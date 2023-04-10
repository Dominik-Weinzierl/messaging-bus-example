import os
import sys
import asyncio
from dotenv import load_dotenv
from nats.aio.client import Client as NatsClient

# Load environment variables from the .env file
load_dotenv()

NATS_URL = os.getenv("NATS_URL")

async def send_message(message):
    nc = NatsClient()
    await nc.connect(NATS_URL)

    await nc.publish("nats.message", message.encode())

    await nc.flush()
    await nc.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        message = sys.argv[1]
        asyncio.run(send_message(message))
    else:
        print("Please provide a message as an argument.")