import typing
import time
import Colors
from NeoTrellisGame import NeoTrellisGame, AbstractNeoTrellisGame, Action
from adafruit_neotrellis.multitrellis import MultiTrellis
from adafruit_neotrellis.neotrellis import NeoTrellis


PLAYER_1 = Colors.RED

PLAYER_2 = Colors.BLUE
TURN = True

class ConnectFour:
    def __init__(self, board: typing.Optional[AbstractNeoTrellisGame] = None):
        self.board = board if board is not None else NeoTrellisGame()
        super().__init__()
        self.game_state = [
            ["c", "c", "c", "c", "c", "c", "c", "b"],
            ["o", "o", "o", "o", "o", "o", "o", "b"],
            ["o", "o", "o", "o", "o", "o", "o", "b"],
            ["o", "o", "o", "o", "o", "o", "o", "b"],
            ["o", "o", "o", "o", "o", "o", "o", "b"],
            ["o", "o", "o", "o", "o", "o", "o", "b"],
            ["o", "o", "o", "o", "o", "o", "o", "b"],  
            ["o", "o", "o", "o", "o", "o", "o", "b"],


        ] #TODO: Choose a structure to represent what pieces are currently in the game board
        self.register_callbacks()
        #self.show_current_player()
        self.show_tie_game()
        
        


        
    def reset_game(self):
        #TODO reset the game state to its original empty state
        self.board.clear_board()
        for r in range(1,len(self.game_state)):
            for c in range(len(self.game_state[r])):
           # self.board.set_callback(c, r, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
                self.board.set_cell_color(c,r, Colors.WHITE)
        #top row back to green
        for col in range(len(self.game_state)):
            self.board.set_callback(col, 0, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
            self.board.activate_key(col, 0, Action.BUTTON_RELEASED) # Even though the callback is set, if the key is not enabled it will not be run. This is how you enable
            self.board.set_cell_color(col,0, Colors.GREEN)
        self.board.update_display()

    def register_callbacks(self):
        #TODO: Register callbacks that will be run when buttons are pressed and released
        self.board.set_callback(0, 0, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
        self.board.activate_key(0, 0, Action.BUTTON_RELEASED) # Even though the callback is set, if the key is not enabled it will not be run. This is how you enable
        #self.board.update_display()
        self.board.set_cell_color(0, 0, Colors.WHITE)
        row = self.game_state[0]

        for col in range(len(row)):
            self.board.set_callback(col, 0, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
            self.board.activate_key(col, 0, Action.BUTTON_PRESSED) # Even though the callback is set, if the key is not enabled it will not be run. This is how you enable
            self.board.set_cell_color(col,0, Colors.GREEN)
        
        #everything else
        for r in range(1,len(row)):
          for c in range(len(self.game_state[r])-1):
            self.board.set_callback(c, r, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
            self.board.set_cell_color(c,r, Colors.WHITE)
        
        self.board.update_display()
        
        

        pass
  
    def handle_button_event(self, x:int, y: int, action: Action):
        """
        This is an example of how a callback function will look. It takes an x value, y value, and action, which will indicate what button activated the callback and what action the user did to run it.
        See NeoTrellisGame.set_callback() for info about callbacks.
        """
        #TODO: Implement what will happen when the button at position x,y is pressed or released
        self.board.set_cell_color(x, y, PLAYER_1)
        self.board.update_display()
        if x == 7 and y==0:
            self.reset_game()
        #self.board.set_cell_color(x, y, PLAYER_1)
        #self.board.update_display()
        global TURN
        if y == 0 and x < 8:


            if self.is_board_full():
                self.show_tie_game()
                pass
            elif self.is_column_full(x):
                pass
            lowest = self.find_lowest_empty_row(x)

            if TURN:
                player = PLAYER_1
                TURN = False
                self.game_state[lowest][x] = "1"
            else:
                player = PLAYER_2
                TURN = True
                self.game_state[lowest][x] = "2"

            self.board.set_cell_color(x,lowest, player)
            self.board.update_display()
                        

            if self.is_board_full():
                show_tie_game()
                pass
            elif self.is_column_full(x):
                pass
            lowest = self.find_lowest_empty_row(x)
            #set new coord to color of player
            #set color to coord
            self.board.set_cell_color(lowest,x, player)
            #check if win
            



        pass
        
        


  
        
    def find_lowest_empty_row(self, col: int):
        #TODO: Return the lowest empty row in the column.
        pass
        for i in range(len(self.game_state) -1):
            last = len(self.game_state) -1 -i
            if self.game_state[last][col] == "o" :
                return last

    def place_piece(self, col: int):
        #TODO: Finds the legal move in the column, and updates the game state to reflect the new piece, checking to see if a player has won with that new piece. Don't forget to play a sound!
        pass

    def update_board_colors(self):
        #TODO: Take the current game state and update the board colors accordingly. Hint: look at NeoTrellisGame.py for functions to update the colors and display the colors
        pass
        self.board.update_display()

    def switch_player(self):
        #TODO: Change which player is curently placing a piece. Keep track of this in some sort of variable
        global TURN
        if TURN :
            TURN = False
        else:
            TURN = True
        pass

    def show_current_player(self):
        #TODO: Function to indicate on the board which player is currently placing a piece
        pass
        global TURN
        if(TURN):
            for col in range(len(self.game_state[0])):
           # self.board.set_callback(col, 0, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
            #self.board.activate_key(col, 0, Action.BUTTON_RELEASED) # Even though the callback is set, if the key is not enabled it will not be run. This is how you enable
                self.board.set_cell_color(col,0, PLAYER_1)
            TURN = FALSE
        else:
            for col in range(len(row)):
           # self.board.set_callback(col, 0, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
            #self.board.activate_key(col, 0, Action.BUTTON_RELEASED) # Even though the callback is set, if the key is not enabled it will not be run. This is how you enable
                self.board.set_cell_color(col,0, PLAYER_2) 
            #TURN = True   

    def is_board_full(self):
        #TODO: Return whether or not the game state has no more legal moves

        for i in self.game_state:
            for j in i:
                if j == "o":
                    return False

                

    def get_player_color(self, player) -> tuple[int, int, int]:
        #TODO: Return the color for the given player 
        if player == PLAYER_1:
            return PLAYER_1
        else:
            return PLAYER_2


    def is_column_full(self, col: int):
        #TODO: Return if the given column is currently full
        if self.game_state[1][col] != "o":
            return True

    def check_win(self):
        #TODO: Check the game state to see if any player has won or if there is a draw
        for i in range(len(self.game_state) -4):
            for j in range (len(self.game_state[0]) -4):
                #diagonal
                if self.game_state[i][j] == self.game_state[i-1][j +1] and self.game_state[i][j] == self.game_state[i-2][j+2] and self.game_state[i][j] == self.game_state[i-3][j+3]:
                    return True
                elif self.game_state[i][j] == self.game_state[i][j +1] and self.game_state[i][j] == self.game_state[i][j +2] and self.game_state[i][j] == self.game_state[i][j +3]:
                    return True
                elif self.game_state[i][j] == self.game_state[i+1][j] and self.game_state[i][j] == self.game_state[i+2][j] and self.game_state[i][j] == self.game_state[i+3][j]:
                    return True
        return False
        

    def show_winner(self):
        #TODO: Display on the board who won
        pass


    def show_tie_game(self):
        #TODO: Display on the board that there was a draw
        pass
        #red
        for r in range(0,4):
          for c in range(len(self.game_state[r])-1):
            #self.board.set_callback(c, r, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
            self.board.set_cell_color(c,r, PLAYER_1)
        #blue
        for row in range(4,len(self.game_state)):
          for col in range(len(self.game_state[row])-1):
            #self.board.set_callback(c, r, self.handle_button_event) # Example of how to register a callback (function) for button 0, 0. Must be done for every button that runs a function
            self.board.set_cell_color(col,row, PLAYER_2)
        
      
   



