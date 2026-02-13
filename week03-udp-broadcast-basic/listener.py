# listener.py with reply
import socket
from config import PORT, BUFFER_SIZE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", PORT))

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"[LISTENER] From {addr}: {data.decode()}")
    
    # Send unicast reply back to sender
    reply = "I am online"
    sock.sendto(reply.encode(), addr)