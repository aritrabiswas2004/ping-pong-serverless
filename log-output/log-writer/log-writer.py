# log-writer.py
import time, random
from datetime import datetime as dt

def gen_random_string(length):
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', k=length))

def write_str_to_file():
    while True:
        with open("/logs/outputs.log", "w") as fileptr:
            fileptr.write(f"{dt.now()}: {gen_random_string(3)}-{gen_random_string(5)}-{gen_random_string(2)}\n")
        time.sleep(5)

if __name__ == '__main__':
    write_str_to_file()
