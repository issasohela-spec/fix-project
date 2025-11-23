import socket
from colorama import init, Fore, Style

init(autoreset=True)  # لضمان إعادة اللون بعد كل طباعة

HOST = "127.0.0.1"
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

print(Fore.CYAN + "[Receiver] Listening on 127.0.0.1:5000 ...")
conn, addr = sock.accept()
print(Fore.GREEN + f"[Receiver] Connection established with {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    fix_message = data.decode().replace("\x01", " | ")
    print(Fore.YELLOW + f"[Receiver] Received: {fix_message}")
