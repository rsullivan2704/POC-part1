"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random
# import codeskulptor
# codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 10000

def nim_trial(num_items):
  is_comp_player = True
  sequence = []
  while num_items > 0:
    random_remove = random.randrange(1, MAX_REMOVE + 1)
    sequence.append((is_comp_player, random_remove))
    num_items -= random_remove
    is_comp_player = not is_comp_player
  return sequence

def evaluate_position(num_items):
  """
  Monte Carlo evalation method for Nim
  """  
  trial = 0
  scores = []
  while trial < TRIALS:
    game_result = nim_trial(num_items)
    if game_result[-1][0] == True:
      # the comp player won the simulation
      # add the value initially chosen
      scores.append(game_result[0][1])
    trial += 1
  moves = {value:scores.count(value) for value in scores}
  move = max(moves, key=moves.get)
  return move


def play_game(start_items):
  """
  Play game of Nim against Monte Carlo bot
  """
  
  current_items = start_items
  print "Starting game with value", current_items
  while True:
    comp_move = evaluate_position(current_items)
    current_items -= comp_move
    print "Computer choose", comp_move, ", current value is", current_items
    if current_items <= 0:
      print "Computer wins"
      break
    player_move = int(input("Enter your current move: "))
    current_items -= player_move
    print "Player choose", player_move, ", current value is", current_items
    if current_items <= 0:
      print "Player wins"
      break

play_game(21)
      
  
                
  