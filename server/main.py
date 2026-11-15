import sqlite3
import time

from flask import Flask, request, jsonify
from flask_cors import CORS

from flask_socketio import SocketIO, emit

# Initialize the DB
conn = sqlite3.connect("game.db")
cursor = conn.cursor()

app = Flask(__name__)
app.config['SECRET_KEY'] = '4' # baller

socketio = SocketIO(app, cors_allowed_origins="http://localhost:5173")

# Enable CORS for local development
CORS(app, resources={r"/api/*": {"origins": "*"}})

@socketio.on('connect')
def handle_connect():
    emit('server_response', {'data': 'Connected!'})

@socketio.on('send_message')
def handle_message(payload):
    emit('recieve_message', payload, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")
# @app.route('/api/get-data', methods=['GET'])
# def get_message():
#     return jsonify({'text': 'Hello from Flask!'})

@app.route('/api/post-update-data', methods=['POST'])
def post_update_data():
    # TODO: Update db
    # TODO: Add check for start / end of game
    data = request.get_json()
    print(data)
    players = data["Players"]
    socketio.emit('player_update', players)
    return {"status": "success", "received": "nonsense"}
    


if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")