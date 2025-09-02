FROM python:3.11

WORKDIR /app

COPY ping-pong.py .

RUN pip install flask psycopg2

CMD ["python3", "ping-pong.py"]

