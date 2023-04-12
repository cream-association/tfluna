import time
import socket

for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    message = b'a'
    addr = ("172.16.10.18", 8080)
    time.sleep(0.2)
    start = time.time()
    client_socket.sendto(message, addr)
time.sleep(1)
client_socket.sendto(b's', addr)
