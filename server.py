from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def handle_message(msg):
    socketio.emit("message", msg)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
