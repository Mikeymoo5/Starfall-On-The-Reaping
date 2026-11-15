import sqlite3
import time

import json

from flask import Flask, request, jsonify
from flask_cors import CORS

from flask_socketio import SocketIO, emit


# Initialize the DB
conn = sqlite3.connect("game.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        health INTEGER
    )
""")
cursor.close()

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

@app.route('/api/game', methods=['POST'])
def post_update_data():
    print("POST")
    # The game sent data
    # TODO: Update db
    # TODO: Add check for start / end of game
    data = request.get_json()
    print(data)
    players = data["Players"]
    socketio.emit('player_update', players) # Transmits the data to the frontend TODO: eventually remove, instead send data to frontend via db

    # Sends data to the db
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    query = """
        INSERT OR REPLACE INTO players (id, username, health)
        VALUES (:id, :Username, :Health)
    """

    rows = ({"id": user_id, **data} for user_id, data in players.items())
    print(rows)
    cursor.executemany(query, rows)
    conn.commit()
    conn.close()
    return {"status": "success"}
    # elif request.content_type == 'GET':
        # return {"status": "success"}
    # return {"status": "failed"}
    
@app.route('/api/player/<int:user_id>', methods=['GET'])
def get_player(user_id):
    # print("hi")

    # data = request.get_json()

    # TODO: Get player id from db

    # Initialize the DB
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM players WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    print(row)
    player_data = {
        "id": row[0],
        "username": row[1],
        "health": row[2],
    }
    return player_data

if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")