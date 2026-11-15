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
cursor.execute("""
    CREATE TABLE IF NOT EXISTS gifts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        player_id ITNEGER NOT NULL,
        item STRING NOT NULL,
        sent BOOL NOT NULL DEFAULT 0 CHECK (sent IN (0, 1))
    )
""")
conn.commit()
conn.close()

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

@app.route('/api/game', methods=['POST', 'GET'])
def post_update_data():
    if request.method == 'POST':
        # The game sent data
        # TODO: Add check for start / end of game
        data = request.get_json()
        print(data)
        players = data["Players"]
        socketio.emit('player_update', players) # Transmits the data to the frontend TODO: eventually remove, instead send data to frontend via db

        # Sends data to the db #TODO: if server does not receive heartbeat for a player who is in the db update their status to be dead (health = 0) 
        # could maybe just set everyone to zero before the insert or replace call?
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
    elif request.method == 'GET':
        # BUG: probably some sort of race condition in here
        conn = sqlite3.connect("game.db")
        cursor = conn.cursor()
        find_row_query = "SELECT * FROM gifts WHERE sent = ?"
        cursor.execute(find_row_query, (0,))

        rows = cursor.fetchall()
        formatted_data = {gift_id: {"recepient_id": recepient_id, "gift_type": gift_type} for (gift_id, recepient_id, gift_type, sent) in rows}
        sent_ids = [(key,) for key in formatted_data]
        print(sent_ids)

        update_sent_query = """
            UPDATE gifts SET sent = 1 WHERE id = ?
        """
        cursor.executemany(update_sent_query, sent_ids)
        conn.commit()
        conn.close()
        return formatted_data
    return "no"

@app.route('/api/player/<int:user_id>', methods=['GET'])
def get_player(user_id):
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

@app.route('/api/send-gift', methods=['POST'])
def send_gift():
    data = request.get_json()
    print(f"heres da data: {data}")

    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()

    query = """
        INSERT INTO gifts (player_id, item, sent)
        VALUES (:player_id, :item, :sent)
    """
    
    cursor.execute(query, data)
    conn.commit()
    conn.close()

    return {"success": "true"}

if __name__ == "__main__":
    app.run(port=5000, debug=True, host="0.0.0.0")