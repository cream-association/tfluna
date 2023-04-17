import time
import socket

addr = ("169.254.23.212", 8080)

print(addr)

for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    message = b'z'
    time.sleep(0.2)
    start = time.time()
    print('send %s'%message.decode('utf-8'))
    client_socket.sendto(message, addr)
time.sleep(1)
client_socket.sendto(b's', addr)
print('send s')
