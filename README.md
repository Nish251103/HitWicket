# Nishchal_21BCE11061




# Chess-Like Game with Web Interface
A turn-based chess-like game with a server-client architecture, utilizing websockets for real-time communication and a web-based user interface

## Getting Started

### Prerequisites
- **Python 3.x**: Ensure Python is installed on your system.
- **Flask**: Install Flask using pip.
- **websocket-client**: Python WebSocket client for handling WebSocket communication.

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the required Python packages:**
   ```bash
   pip install Flask websocket-client
   ```

### Running the Application
1. **Start the Flask server:**
   ```bash
   python app.py
   ```

   The Flask server will start on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

2. **WebSocket Client:**
   - The WebSocket client runs in a separate thread and connects to a WebSocket server. Modify the WebSocket server URL in the `run_websocket_client` function as needed.

### Project Structure
```
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Main HTML file rendered by Flask
├── static/
│   └── (Optional)         # Static files like CSS or JavaScript if needed
├── README.md              # This file
└── requirements.txt       # Python dependencies (optional)
```

### API Endpoints
- **GET /game_state**: Retrieve the current game state.
- **POST /select_piece**: Validate the selection of a piece.
  - **Request Body:**
    ```json
    {
      "row": <int>,
      "col": <int>
    }
    ```
- **POST /move_piece**: Make a move with the selected piece.
  - **Request Body:**
    ```json
    {
      "x": <int>,
      "y": <int>,
      "move": <str>
    }
    ```

### How to Play
1. Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
2. Player 1 and Player 2 take turns to move their pieces on the board.
3. The first player to capture 5 of the opponent's pieces wins the game.

### Customizing the Game
- **Board Size**: You can change the board size by modifying the `BOARD_SIZE` constant in `app.py`.
- **Piece Movement**: Modify the `move_piece` function to customize the movement rules for each piece.

### WebSocket Integration
- The WebSocket client connects to a server specified in the `run_websocket_client` function. It can be used for real-time communication, such as broadcasting game events or syncing game states between multiple clients.

### Troubleshooting
- **WebSocket Issues**: Ensure the WebSocket server URL is correct and that the server is running.
- **Flask Errors**: Check that all required dependencies are installed and that the Flask server is running without issues.

### Contributing
If you wish to contribute, please fork the repository and submit a pull request. Bug reports and feature requests are welcome.

---

Feel free to customize any part of this README file to better suit your project specifics!
