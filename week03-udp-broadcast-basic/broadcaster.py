# broadcaster.py with collection
import socket
import time
from config import BROADCAST_IP, PORT, BUFFER_SIZE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("", PORT))  # Also listen for replies

# Send broadcast
sock.sendto(b"DISCOVERY: Who is online?", (BROADCAST_IP, PORT))
print("[BROADCASTER] Discovery sent")

# Wait for replies
sock.settimeout(2)
responses = []
while True:
    try:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        responses.append(addr)
        print(f"[BROADCASTER] Reply from {addr}: {data.decode()}")
    except socket.timeout:
        break

print(f"[BROADCASTER] Total responses: {len(responses)}")