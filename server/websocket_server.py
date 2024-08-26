import asyncio
import websockets
import json
from flask import Flask, render_template
from game import Game

app = Flask(__name__, template_folder='../client/templates')
game = Game()

# Flask route to serve the web interface
@app.route('/')
def index():
    return render_template('index.html')

async def handle_client(websocket, path):
    while True:
        message = await websocket.recv()
        data = json.loads(message)
        action = data.get('action')

        if action == 'init':
            game_state = game.initialize_game()
            await websocket.send(json.dumps(game_state))
        
        elif action == 'move':
            player = data['player']
            char = data['character']
            direction = data['direction']
            result = game.move(player, char, direction)
            await websocket.send(json.dumps(result))
        
        if game.game_over:
            break

start_server = websockets.serve(handle_client, "localhost", 8765)

if __name__ == "__main__":
    # Run WebSocket server in the background
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server)

    # Run Flask app to serve the web interface
    app.run(host='0.0.0.0', port=5001)
