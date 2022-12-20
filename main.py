# Create class for game
class Game:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.player = None
        self.x_coord = None
        self.y_coord = None
        self.win = None

    def get_coords(self):
        self.x_coord = int(input("Enter row number for chosen cell: ")) - 1
        self.y_coord = int(input("Enter column number for chosen cell: ")) - 1

    def check_coords(self):
        if self.board[self.x_coord][self.y_coord] == " ":
            self.board[self.x_coord][self.y_coord] = str(self.player)
            self.print_board()
        else:
            while self.board[self.x_coord][self.y_coord] != " ":
                print("Error, cell is already occupied. Please try again.\n")
                self.get_coords()
            if self.board[self.x_coord][self.y_coord] == " ":
                self.board[self.x_coord][self.y_coord] = str(self.player)
                self.print_board()

    def print_board(self):
        for i, row in enumerate(self.board):
            print('|'.join([' {} '.format(cell) for cell in row]))
            if i < len(self.board) - 1:
                print('-----------')

    def play_cell(self):
        print(f"{self.player}, select an area to place a symbol")
        self.get_coords()
        self.check_coords()

    def computer_play_cell(self):
        print("Computer is choosing...")
        self.board[self.x_coord][self.y_coord] = "O"
        self.print_board()

    def is_winner(self):
        # check rows
        for row in self.board:
            if all(cell == self.player for cell in row):
                return True
        # check columns
        for col in range(3):
            if all(self.board[row][col] == self.player for row in range(3)):
                return True
        # check diagonals
        if all(self.board[i][i] == self.player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == self.player for i in range(3)):
            return True
        # no win
        return False

    def play_game(self):
        self.print_board()
        i = 1
        while i < 10:
            if i % 2 == 1:
                self.player = "X"
                self.play_cell()
                self.win = self.is_winner()
                if self.win:
                    print("Player X is the winner!")
                    break
                else:
                    if i == 9:
                        if self.win is False:
                            print("Draw!")
                            break
                    else:
                        i += 1
            if i % 2 == 0:
                self.player = "O"
                # FOR COMPUTER
                self.x_coord, self.y_coord = self.determine_o_move()
                self.computer_play_cell()
                self.win = self.is_winner()
                if self.win:
                    print("Player O is the winner!")
                    break
                else:
                    i += 1

    def determine_o_move(self):
        # check for a winning move
        self.player = "O"
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    if self.is_winner():
                        return i, j
                    self.board[i][j] = ' '

        # check for a blocking move
        self.player = "X"
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'X'
                    if self.is_winner():
                        return i, j
                    self.board[i][j] = ' '

        # play in the center
        if self.board[1][1] == ' ':
            return 1, 1

        # play in a corner
        for i in [0, 2]:
            for j in [0, 2]:
                if self.board[i][j] == ' ':
                    return i, j

        # play in any remaining empty cell
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return i, j

# Run
if __name__ == '__main__':
    print("Starting new game...")
    newGame = Game()
    newGame.play_game()
