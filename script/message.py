import os
import asyncio
import argparse
from dotenv import load_dotenv
from nats.aio.client import Client as NatsClient

# Load environment variables from the .env file
load_dotenv()

NATS_URL = os.getenv("NATS_URL")

async def send_message(subject, message):
    nc = NatsClient()
    await nc.connect(NATS_URL, nkeys_seed="./user.nk")
    
    await nc.publish(subject, message.encode())

    await nc.flush()
    await nc.close()

def parse_args():
    parser = argparse.ArgumentParser(description="Send a message using NATS")
    parser.add_argument('-s', '--subject', help='Subject of the message', required=True)
    parser.add_argument('-m', '--message', help='Message to be sent', required=True)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    asyncio.run(send_message(args.subject, args.message))