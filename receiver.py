import os
import socket

# File to send
file_path = "procexp64.exe"
file_size = os.path.getsize(file_path)

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

# Send file name and size
client.send("transferred.exe".encode())
client.send(str(file_size).encode())

# Send file data
with open(file_path, "rb") as file:
    data = file.read()
    client.sendall(data)

print("File sent successfully.")
client.close()
