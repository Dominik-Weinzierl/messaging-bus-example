import os
import asyncio
import argparse
from dotenv import load_dotenv
from nats.aio.client import Client as NatsClient

# Load environment variables from the .env file
load_dotenv()

NATS_URL = os.getenv("NATS_URL")

async def on_message(msg):
    data = msg.data.decode()
    print(f"Received a message: {data}")

async def on_connect(subject):
    nc = NatsClient()
    await nc.connect(NATS_URL, nkeys_seed="./server.nk")

    print("Connected to NATS")
    await nc.subscribe(subject, cb=on_message)

    # Keeps the connection alive; you may want to adjust this for your use case
    while True:
        await asyncio.sleep(1)

def parse_args():
    parser = argparse.ArgumentParser(description="Listen to messages on a given subject using NATS")
    parser.add_argument('-s', '--subject', help='Subject to listen for messages', required=True)
    return parser.parse_args()

async def main(subject):
    print("Starting server...")
    print("Listening for messages on subject: {}".format(subject))
    
    tasks = [
        asyncio.create_task(on_connect(subject))
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    args = parse_args()
    asyncio.run(main(args.subject))