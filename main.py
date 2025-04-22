import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen(1)
print("Server is listening on port 9999...")

conn, addr = server.accept()
print(f"Connected by {addr}")

# Receive filename
filename = conn.recv(1024).decode()
print(f"Receiving file: {filename}")

# Receive file size
file_size = int(conn.recv(1024).decode())
print(f"Expected file size: {file_size} bytes")

# Receive file data
with open(filename, "wb") as f:
    received = 0
    while received < file_size:
        data = conn.recv(4096)
        if not data:
            break
        f.write(data)
        received += len(data)

print("File received successfully.")
conn.close()
server.close()
