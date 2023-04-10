# NATS Messaging Project

This project demonstrates how to send and receive messages using NATS, with separate Python scripts for sending messages and running a server that listens for messages.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository.

```console
git clone git@github.com:Dominik-Weinzierl/messaging-bus-example.git
cd messaging-bus-example
```

2. Build the Docker images.

```console
docker-compose build
```

3. Start the NATS server and the message listener server using Docker Compose.

```console
docker-compose up
```

The NATS server and message listener server should now be running. The listener server will output the received messages to the console.

## Sending Messages

To send messages, you'll need to install the Python dependencies locally:

1. Install the required Python packages (in a venv).

```console
pip install -r scripts/requirements.txt
```

2. Run the `message.py` script with the message you want to send as a command-line argument.

```console
python scripts/message.py "Hello, this is my message!"
```

The message will be sent to the NATS server, and the message listener server should display the received message in the console.