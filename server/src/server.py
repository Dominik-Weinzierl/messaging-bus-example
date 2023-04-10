import os
import asyncio
from dotenv import load_dotenv
from nats.aio.client import Client as NatsClient

# Load environment variables from the .env file
load_dotenv()

NATS_URL = os.getenv("NATS_URL")

async def on_message(msg):
    data = msg.data.decode()
    print(f"Received a message: {data}")
    
    # Process the message and insert it into the SQL database here

async def on_connect():
    nc = NatsClient()
    await nc.connect(NATS_URL)

    print("Connected to NATS")
    await nc.subscribe("nats.message", cb=on_message)

    # Keeps the connection alive; you may want to adjust this for your use case
    while True:
        await asyncio.sleep(1)

async def main():
    print("Starting server...")
    
    # Print environment variables for debugging
    print(f"NATS_URL: {NATS_URL}")
    
    tasks = [
        asyncio.create_task(on_connect())
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
