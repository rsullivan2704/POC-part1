"""
Monte Carlo Tic-Tac-Toe Player
"""

import poc_ttt_provided as provided
import random
#import poc_ttt_gui

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player):
  '''
  Randomly plays the game starting with the given player and the given
  board state.
  '''
  if board.check_win() == None:
    # game is in progress, fill empty squares with random moves
    empties = board.get_empty_squares()
    while len(empties) > 0:
      random_square = empties.pop(random.randrange(0, len(empties)))
      board.move(random_square[0], random_square[1], player)
      player = provided.switch_player(player)
      if board.check_win() != None:
        # The game ended with a winner or a draw, stop playing 
        break
    
def mc_update_scores(scores, board, player):
  '''
  Updates the given scores grid based on the winner of the game.
  '''
  winner = board.check_win()
  if winner != provided.DRAW:
    factor = 1
    if winner != player:
      # negate the factor so in effect the score is deducted
      # if the machine player is not the winner
      factor = -1
    for row_idx, row in enumerate(board):
      for col_idx, square in enumerate(row):
        if square != provided.EMPTY:
          if square == player:
            scores[row_idx][col_idx] += (factor * SCORE_CURRENT)
          else:
            scores[row_idx][col_idx] -= (factor * SCORE_OTHER)
    
def get_best_move(board, scores):
  '''
  Randomly return the best move based on the scores provided.
  '''
  empties = board.get_empty_squares()
  max_score = 0
  for empty_square in empties:
    current_max = scores[empty_square[0]][empty_square[1]]
    if current_max > max_score:
      max_score == current_max
  while len(empties) > 0:
    random_square = empties.pop(random.randrange(0, len(empties)))
    if scores[random_square[0]][random_square[1]] == max_score:
      return random_square
    
def mc_move(board, player, trials):  
  '''
  Returns a (row, col) tuple representing the best move to an empty square
  on the board. 
  '''
  scores = [[0 for dummycol in range(board.get_dim())]
            for dummyrow in range(board.get_dim())]
  for trial in range(trials):
    trial_board = board.clone()
    mc_trial(trial_board, player)
    mc_update_scores(scores, board, player)
  return get_best_move(board, scores)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
