# server.py
from fastapi import FastAPI
import socket
import time

app = FastAPI()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 9999)
server_socket.bind(server_address)
server_socket.listen(5)


@app.post('/send_message')
async def send_message(message: str):
    client_socket, client_address = server_socket.accept()
    client_socket.sendall(message.encode())
    client_socket.sendall(message.encode()) 
    return {"status": "success", "message": f"Sent message to clients: {message}"}
