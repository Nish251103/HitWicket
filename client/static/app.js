let ws = new WebSocket("ws://localhost:8765");

ws.onopen = () => {
    ws.send(JSON.stringify({action: "init"}));
};

ws.onmessage = (event) => {
    let data = JSON.parse(event.data);
    if (data.error) {
        alert(data.error);
    } else if (data.message) {
        document.getElementById('status').innerText = data.message;
    } else {
        renderBoard(data.board);
        document.getElementById('status').innerText = "Current turn: " + data.turn;
    }
};

function renderBoard(board) {
    let html = "<table>";
    for (let i = 0; i < board.length; i++) {
        html += "<tr>";
        for (let j = 0; j < board[i].length; j++) {
            let cell = board[i][j];
            html += `<td class="${cell.charAt(0)}">${cell}</td>`;
        }
        html += "</tr>";
    }
    html += "</table>";
    document.getElementById('game-board').innerHTML = html;
}

function makeMove(player, char, direction) {
    ws.send(JSON.stringify({
        action: "move",
        player: player,
        character: char,
        direction: direction
    }));
}
