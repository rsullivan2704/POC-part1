"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
#import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board:provided.TTTBoard, player):
    empties = board.get_empty_squares()
    while len(empties) > 0:
      random_square = empties.pop(random.randrange(0, len(empties)))
      board.move(random_square[0], random_square[1], player)
      player = provided.switch_player(player)
    
def mc_update_scores(scores:list, board:provided.TTTBoard, player):
    for row_idx, row in enumerate(board):
      for col_idx, square in enumerate(row):
        if square != provided.EMPTY:
          if square == player:
            scores[row_idx][col_idx] -= SCORE_CURRENT
          else:
            scores[row_idx][col_idx] += SCORE_OTHER
    
def get_best_move(board:provided.TTTBoard, scores):
    pass
    
def mc_move(board:provided.TTTBoard, player, trials):  
    pass

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
