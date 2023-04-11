FROM python:3.9

COPY src/ /app/src
COPY .env /app/.env
COPY server.nk /app/server.nk
COPY requirements.txt /app/requirements.txt

WORKDIR /app

# Update pip
RUN python3 -m pip install --upgrade pip

# Install required packages
RUN pip3 install -r /app/requirements.txt

CMD ["python3", "-u", "src/server.py", "-s", "nats.message"]
