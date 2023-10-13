class TicTacToeLogic:
    def __init__(self):
        self.player1 = "X"
        self.player2 = "O"
        self.empty = " "
        self.board_size = self.get_board_size()
        self.board = [[self.empty for _ in range(self.board_size)] for _ in range(self.board_size)]   # Creating certain size game board


    def get_board_size(self):
        while True:
            try:
                board_size = int(input("Enter the board size (e.g. 3 for a 3x3 board): "))
                if board_size < 3:
                    print("Board size must be at least 3.")
                else:
                    return board_size
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    '''Function to check for a win'''
    def check_win(self):
        win_conditions = [[(i, j) for j in range(self.board_size)] for i in range(self.board_size)] +\
                         [[(i, j) for i in range(self.board_size)] for j in range(self.board_size)] +\
                         [[(i, i) for i in range(self.board_size)]] +\
                         [[(i, self.board_size - 1 - i) for i in range(self.board_size)]]

        for win_condition in win_conditions:
            values= [self.board[i][j] for i,j in win_condition]
            if all(value == values[0] != self.empty for value in values):
                return True, values[0]
        return False, None

    '''Function to check for a tie'''
    def check_tie(self):
        return all(self.board[i][j] != self.empty for i in range(self.board_size) for j in range(self.board_size))
        # if all elements in an iterable are 'True' return True, otherwise 'False'

    ''' Function to update the board with player's move'''
    def update_board(self, move, player):
        row, col = move // self.board_size, move % self.board_size
        if self.board[row][col] == self.empty:     # if the coordinate is empty
            self.board[row][col] = player
        else:
            raise ValueError("Invalid move. the selected cell is already occupied.")

    def get_current_player(self):
        empty_cells_count = sum(row.count(self.empty) for row in self.board)
        if empty_cells_count % 2 == 1:   # if empty_cells is odd number -> player1, otherwise player2
            return self.player1   # "X"
        else:
            return self.player2   # "O"



