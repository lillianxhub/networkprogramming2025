# broadcaster.py with periodic sending
import socket
import time
from config import BROADCAST_IP, PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
    message = f"DISCOVERY: {time.strftime('%H:%M:%S')}"
    sock.sendto(message.encode(), (BROADCAST_IP, PORT))
    print(f"[BROADCASTER] Sent: {message}")
    time.sleep(5)  # Every 5 seconds