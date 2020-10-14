import threading
import socket

PORT = 5050
#SERVER = "192.168.8.100"

SERVER = socket.gethostbyname(socket.gethostname())

print(SERVER)