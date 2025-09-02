from flask import Flask
import psycopg2
import time
import os

app = Flask(__name__)

def get_connection():
    global conn
    global cur

    while True:
        try:
            conn = psycopg2.connect(
                host="postgres-svc",
                port=5432,
                dbname="pongsdb",
                user="postgres",
                password="postgres"
            )
            cur = conn.cursor()
            break
        except psycopg2.OperationalError:
            print("Trying again")
            time.sleep(2)

get_connection()

def init_db():
    cur.execute("CREATE TABLE IF NOT EXISTS pongs (pong_count int)")

    cur.execute("SELECT COUNT(*) FROM pongs")
    count = cur.fetchone()[0]

    if count == 0:
        cur.execute("INSERT INTO pongs (pong_count) VALUES (0)")

    conn.commit()

init_db()

def write_pongs_to_db():
    try:
        cur.execute("UPDATE pongs SET pong_count = pong_count + 1")
    except Exception as e:
        print("Exception Occurred -> ", e)

def read_pongs_from_db():
    cur.execute("SELECT * FROM pongs")
    value = cur.fetchall()[0][0]

    return value

@app.route('/healthz')
def health_state():
    try:
        cur.execute("SELECT 1")
        return ("ok", 200)
    except:
        return ("db conn failed", 500)


@app.route('/pings')
def get_pings():
    count = read_pongs_from_db()
    return f"Ping / Pongs: {count}" if count > 0 else "Ping / Pongs: No pingi-pongo yet!"

@app.route('/')
def hello():
    write_pongs_to_db()
    return f"pong {read_pongs_from_db()}", {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run("0.0.0.0", port=os.environ.get('MYPORT', 8080))
