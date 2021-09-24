import db

class Gameboard():
    def __init__(self):
        self.player1 = ""
        self.player2 = ""
        self.board = [[0 for x in range(7)] for y in range(6)]
        self.game_result = ""
        self.current_turn = 'p1'
        self.remaining_moves = 42
<<<<<<< Updated upstream
    
=======
        self.index_map = {
            "col1": 5,
            "col2": 5,
            "col3": 5,
            "col4": 5,
            "col5": 5,
            "col6": 5,
            "col7": 5
        }

    '''
    Logic for handleing a players move.
    Returns a value justifying the move.
    test
    '''

    def move(self, player, col):
        col_idx = int(col[3]) - 1
        reason = self.valid_move(player, col)
        if reason == "OK":
            self.place_move(col, col_idx)
            self.after_move()
        return reason

    '''
    Checks if the player made a valid move.
    '''

    def valid_move(self, player, col):

        # Checks if the game is already over
        if self.game_result != "":
            return "Game is over."

        # Checks if it's the players turn
        elif self.current_turn != player:
            return "It is not your turn."

        # Checks if the column is full
        elif self.index_map[col] < 0:
            return "Illegal Move."

        # Move is valid
        else:
            return "OK"

    '''
    Updates the board with the players move.
    '''

    def place_move(self, col, col_idx):
        open_idx = self.index_map[col]
        self.index_map[col] -= 1
        self.board[open_idx][col_idx] = self.player1 if self.current_turn == 'p1' else self.player2

    '''
    Handles all loginc for finishing a move.
    '''

    def after_move(self):

        # Check winner
        self.check_winner()

        # Change turn
        self.current_turn = 'p1' if self.current_turn == 'p2' else 'p2'

        # Change moves remaining
        self.remaining_moves -= 1

        # Check moves remaining
        if self.remaining_moves <= 0:
            self.game_result = 'Draw'

    '''
    Checks if the played move resulted in a win.
    '''

    def check_winner(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.check_horizontal(i, j) or self.check_vertical(i, j) or self.check_diagonal_down(i, j) or self.check_diagonal_up(i, j):
                    self.game_result = self.current_turn

    '''
    Checks horizontal wins.
    '''

    def check_horizontal(self, i, j):

        # Check bounds of array
        if j + 3 > len(self.board[0]) - 1:
            return False

        # Get 4 horizontal colors
        color1 = self.board[i][j]
        color2 = self.board[i][j + 1]
        color3 = self.board[i][j + 2]
        color4 = self.board[i][j + 3]

        # Check that the current index is played and all other colors match
        if color1 != 0 and color1 == color2 == color3 == color4:
            return True
        return False

    '''
    Checks vertical wins.
    '''

    def check_vertical(self, i, j):

        # Check bounds of array
        if i + 3 > len(self.board) - 1:
            return False

        # Get 4 vertical colors
        color1 = self.board[i][j]
        color2 = self.board[i + 1][j]
        color3 = self.board[i + 2][j]
        color4 = self.board[i + 3][j]

        # Check that the current index is played and all other colors match
        if color1 != 0 and color1 == color2 == color3 == color4:
            return True
        return False

    '''
    Checks diagonal downwards wins.
    '''

    def check_diagonal_down(self, i, j):

        # Check bounds of array
        if i - 3 < 0 or j + 3 > len(self.board[0]) - 1:
            return False

        # Get 4 diagonal down colors
        color1 = self.board[i][j]
        color2 = self.board[i - 1][j + 1]
        color3 = self.board[i - 2][j + 2]
        color4 = self.board[i - 3][j + 3]

        # Check that the current index is played and all other colors match
        if color1 != 0 and color1 == color2 == color3 == color4:
            return True
        return False

    '''
    Checks diagonal upwards wins.
    '''

    def check_diagonal_up(self, i, j):
        # Check bounds of array
        if i + 3 > len(self.board) - 1 or j + 3 > len(self.board[0]) - 1:
            return False

        # Get 4 diagonal up colors
        color1 = self.board[i][j]
        color2 = self.board[i + 1][j + 1]
        color3 = self.board[i + 2][j + 2]
        color4 = self.board[i + 3][j + 3]
>>>>>>> Stashed changes

'''
Add Helper functions as needed to handle moves and update board and turns
'''


    
