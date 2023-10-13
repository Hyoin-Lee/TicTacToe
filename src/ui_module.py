from logic_module import TicTacToeLogic

class TicTacToeUI:
    def __init__(self):
        self.logic = TicTacToeLogic()

    # Function to print the board
    def print_board(self):
        for row in self.logic.board:
            print(" | ".join(row))  # give a separation for each cell in a row
            print("---------")          # give a separation between row

    # Function to get the next move from the player
    def get_next_move(self, player):
        while True:
            try:
                move = int(input(f"Next move for player {player} (0-8):  "))  # convert input to integer
                if 0 <= move <= 8:
                    return move
                else:
                    print("Invalid move, try again.")
            except ValueError:  # if input is not integer
                print("Invalid type, try again with number between (0-8).")

        # Game loop
    def run_game(self):
        while True:
            # Print board
            self.print_board()
            print()

            # Check for win
            is_win, winner = self.logic.check_win()   # return two value, which is True or False and player(winner)
            if is_win:
                print("Player", winner, "wins!")
                break

            # Check for tie
            if self.logic.check_tie():    # return True or False
                print("It's a tie!")
                break

            # Get next move
            player = self.logic.get_current_player()   # return player
            move = self.get_next_move(player)    # return move

            if self.logic.update_board(move, player):
                pass
            else:
                print("Invalid move, try again.")

if __name__ == "__main__":
        ui = TicTacToeUI()
        ui.run_game()