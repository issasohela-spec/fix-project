from colorama import init, Fore
import socket
import time
import random

init(autoreset=True)

HOST = "127.0.0.1"
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

print(Fore.CYAN + "[Sender] Connected to receiver.")

def build_fix_message():
    price = round(random.uniform(1.0800, 1.1200), 5)
    msg = f"8=FIX.4.4|35=W|55=EUR/USD|270={price}|10=000|"
    msg = msg.replace("|", "\x01")
    return msg

while True:
    fix_msg = build_fix_message()
    sock.send(fix_msg.encode())
    print(Fore.MAGENTA + f"[Sender] Sent: {fix_msg.replace(chr(1), ' | ')}")
    time.sleep(1)
