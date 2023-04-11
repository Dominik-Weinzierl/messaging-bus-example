# NATS Messaging Project

This project demonstrates how to send and receive messages using the NATS messaging system with separate Python scripts for sending messages and running a server that listens for messages. The project uses NKEY-based authentication to restrict permissions for different clients.

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

The NATS server and message listener server should now be operational. The listener server will display the received messages on the console. The server user is granted permission to subscribe to messages, but is restricted from publishing messages.

## Sending Messages

To send messages, you'll need to install the Python dependencies locally:

1. Install the required Python packages (in a venv).

```console
pip install -r scripts/requirements.txt
```

2. Run the `message.py` script with the message you want to send as a command-line argument.

```console
$ python3 scripts/message.py -h                          
usage: message.py [-h] -s SUBJECT -m MESSAGE

Send a message using NATS

optional arguments:
  -h, --help            show this help message and exit
  -s SUBJECT, --subject SUBJECT
                        Subject of the message
  -m MESSAGE, --message MESSAGE
                        Message to be sent
```

```console
python scripts/message.py -s nats.message -m "Hello, this is my message!"
```

The message will be sent to the NATS server, and the message listener server should display the received message in the console. The messaging user is granted permission to publish messages, but is restricted from subscribing to messages.