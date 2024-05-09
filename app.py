from flask import Flask
from flask.ext.socketio import SocketIO, emit
host = '127.0.0.1'
port = 50001

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()