from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)] # we will use a single list to represent 3x3 board
        self.CurrentWinner = None #Keep track of winner

    def print_board(self):
        for row in [self.board[i*3 : (i+1)*3] for i in range(3) ]:
            print("| " + "| " .join(row) + "| " )


    @staticmethod
    def print_board_nums():
        # 0| 1| 2 etc tells us what number corresponds to each box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + "| " .join(row) + "| ")

    def available_moves(self):
         return[i  for i, spot in enumerate(self.board) if spot == " "]
    
    def empty_squares(self):
        return " " in self.board
    
    def num_empty_squares(self):
        return self.board.count(" ")
        # return len(self.available_moves())
        #moves = []
        #for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0,"x"), (1, "x"), (2, "o")]
            #if spot == " ":
                #moves.append(i)
        #return moves 
    
    def make_move(self, square, letter):
        #if valid move then make the move (assign square to letter)
        #then return true .  If invalid, return false

        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.CurrentWinner = letter
            return True
        return False

    def winner(self, square, letter):
        #winner if 3 in a row anywhere
        #to check the row:

        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        #check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check diagonals
        #but only if the square is an even number(0, 2, 4, 6, 8)
        #these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i]for i in [ 0, 4, 8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i]for i in [ 2, 4, 6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        #if all these checks fail:
        return False



def play(game, x_player, o_player, print_game=True ):
    #Returns the winner of the game or none for a tie
    if print_game:
        game.print_board_nums()
    letter = "X"
    # iterate while game has empty squares
    # we dont have to worry abt the winner we'll just return that which breaks the loop
    while game.empty_squares():
        #get the move from the appropaite player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #now to craete function to make move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f"makes a move to square {square}")
                game.print_board()
                print(" ")  #just an empty line

            if game.CurrentWinner:
                if print_game:
                    print(letter + "wins!")
                return letter


            # To alternate letters:
            if letter == "X":
                letter = "O"
            else:
                 letter = "X"

           
           #letter ="O" if letter == "X" else "X"
        #to make it pause a little
        if print_game:
            time.sleep(0.8)
    if print_game:
            print("It's a tie")

if __name__ == "__main__":
    x_wins = 0
    o_wins = 0
    ties = 0
    start = time.time()
    for _ in range(100):

        x_player = HumanPlayer("X")           
        o_player = RandomComputerPlayer("O")
        t  = TicTacToe()
        result = play(t, x_player, o_player, print_game = True ) 
        if result == "X":
            x_wins += 1
        elif result == "O":
            o_wins +=1
        else:
            ties += 1
    end = time.time()
print(f"After a thousand iterations, we see:{x_wins} X wins, {o_wins} O wins, {ties} Ties, Time taken:{end-start} ")

        #play(t, x_player, o_player, print_game = False ) 


