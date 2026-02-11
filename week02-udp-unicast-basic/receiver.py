# receiver.py
import socket
from config import HOST, PORT, BUFFER_SIZE

received_ids = set()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    msg_id, text = data.decode().split('|', 1)
    msg_id = int(msg_id)
    
    if msg_id in received_ids:
        print(f"[RECEIVER] Duplicate: {msg_id}")
    else:
        received_ids.add(msg_id)
        print(f"[RECEIVER] New: {msg_id} -> {text}")