from flask import Flask, render_template
import random
import socket
from flask_socketio import SocketIO
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"

@app.route('/<name>')
def group(name):
    return 'Welcome to the {} room!'.format(name)

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host,port))


    message = input(">> ")

    while message.lower().strip()!="quit":
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print("Response from Server : "+str(data))
        message = input(">> ")
    client_socket.close()

if __name__ == "__main__":
    app.run()