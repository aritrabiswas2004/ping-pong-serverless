from flask import Flask
import requests
import os

app = Flask(__name__)

def read_pongs():
    try:
        response = requests.get("http://my-ping-pong.exercises.172.18.0.3.sslip.io/pings") # change this

        if response.status_code == 200:
            return response.content.decode() # f"{response.content}"
        else:
            return f"STATUS: {response.status_code} -- Something went wrong"
    except Exception as e:
        return f"ERROR -> {e}"

def read_contents():
    try:
        with open("/logs/outputs.log", "r") as fileptr:
            return fileptr.read()
    except FileNotFoundError:
        return "No logs yet"

def env_message():
    return f"env variable: MESSAGE={os.environ.get('message', 'message env does not exist')}"

def file_message():
    with open("/config/information.txt", "r") as fileptr:
        contents = fileptr.read()

    return f"file content: {contents}"

@app.route('/healthz')
def check_ping_pong_health():
    response = requests.get("http://my-ping-pong.exercises.172.18.0.3.sslip.io/pings")

    if response.status_code == 200:
        return ("all ok", 200)

    return ("ping-pong not ready", 500)

@app.route('/')
def main():
    return f"{file_message()}\n{env_message()}\n{read_contents()}\n{read_pongs()}", {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run("0.0.0.0", port=os.environ.get('MYPORT', 8080))

