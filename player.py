import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    # for player to get next move    
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\"s turn. Input move(0-8):")
            # we're gonna chech this is a valid input by trying to cast it to an integer if its not then we say invalid input
            #if that spot is not availabel on the board we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            
            except ValueError:
                print ('Invalid square, Try again')

        return val 

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            #get the square based on the minimax algorithm
            square = self.minimax(game, self.letter)["position"]
        return square
    def minimax(self, state, player):
        max_player = self.letter #yourself
        other_player = "O" if player == "X" else "X" #the other player (computer)

        #first check if the previous move was a winner 
        #this is the base case (where we currentle are)
        if state.CurrentWinner == other_player:
            #we should return position and score because we need to keep track of the score for minimax to work
            return{"position":None, "score": 1 * (state.num_empty_squares() + 1) if other_player == max_player 
                   else -1*(state.num_empty_squares() + 1)}
        
    
        elif not state.empty_squares():
            #no empty sqaures
            return {"position":None, "score":0}
        
        if player == max_player:
            best = {"position": None, "score": -math.inf} #each score should maximize (be larger )
        else:
            best = {"position": None, "score": math.inf} #each score should minimize

        for possible_move in state.available_moves():
            #step 1 : make a move , try that spot
            state.make_move(possible_move, player)
            #step 2 : recurse using minimax to simulate a game using that move
            sim_score = self.minimax(state, other_player) #now, we alternate players

            #step 3 : undo the move
            state.board[possible_move] = " "
            state.CurrentWinner = None 
            sim_score["position"] = possible_move #will get messed up if not because of the recursion

            #step 4: update the dictionaries if needed
            if player == max_player: #trying to maximize the max_player
                if sim_score["score"] > best["score"]:
                    best = sim_score  #replaces best
            else: #but minimize the other player
                if sim_score["score"] < best["score"]:
                    best = sim_score #replaces best 

        return best





        
