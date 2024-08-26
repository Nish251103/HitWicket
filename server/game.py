class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(5)] for _ in range(5)]
        self.players = {'A': [], 'B': []}
        self.turn = 'A'
        self.game_over = False

    def initialize_game(self):
        self.players['A'] = ['A-P1', 'A-H1', 'A-H2', 'A-P2', 'A-P3']
        self.players['B'] = ['B-P1', 'B-H1', 'B-H2', 'B-P2', 'B-P3']
        self.board[0] = self.players['A']
        self.board[4] = self.players['B']
        return self.get_game_state()

    def move(self, player, char, direction):
        if self.turn != player or self.game_over:
            return {"error": "Not your turn or game over"}
        
        # Find character's position
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == f'{player}-{char}':
                    x, y = i, j
                    break
        
        # Move logic
        if char == 'P':  # Pawn moves one block
            if direction == 'L':
                y -= 1
            elif direction == 'R':
                y += 1
            elif direction == 'F':
                x -= 1
            elif direction == 'B':
                x += 1
        elif char == 'H1':  # Hero1 moves two blocks straight
            if direction == 'L':
                y -= 2
            elif direction == 'R':
                y += 2
            elif direction == 'F':
                x -= 2
            elif direction == 'B':
                x += 2
        elif char == 'H2':  # Hero2 moves two blocks diagonally
            if direction == 'FL':
                x -= 2
                y -= 2
            elif direction == 'FR':
                x -= 2
                y += 2
            elif direction == 'BL':
                x += 2
                y -= 2
            elif direction == 'BR':
                x += 2
                y += 2
        
        # Validate move
        if x < 0 or x >= 5 or y < 0 or y >= 5:
            return {"error": "Invalid move"}
        
        # Combat
        if self.board[x][y] != ' ':
            self.board[x][y] = f'{player}-{char}'
            if player == 'A':
                self.players['B'].remove(self.board[x][y])
            else:
                self.players['A'].remove(self.board[x][y])
        else:
            self.board[x][y] = f'{player}-{char}'
        
        self.board[i][j] = ' '
        self.turn = 'B' if self.turn == 'A' else 'A'

        # Check for win condition
        if not self.players['A'] or not self.players['B']:
            self.game_over = True
            return {"message": f"Player {player} wins!"}
        
        return self.get_game_state()

    def get_game_state(self):
        return {"board": self.board, "turn": self.turn}
