FROM python:3.11

WORKDIR /app

COPY log-reader.py .

RUN pip install flask requests

EXPOSE 3000

CMD ["python3", "log-reader.py"]

