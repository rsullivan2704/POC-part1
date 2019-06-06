import poc_simpletest
import solitaire_mancala_test_suite
import solitaire_mancala_test_cases

class SolitaireMancala: 
  def __init__(self): 
    self.game_board = [0] 
    
  def set_board(self, configuration): 
    self.game_board = configuration[::] 
    
  def __str__(self): 
    game_board = self.game_board[::] 
    game_board.reverse() 
    return str(game_board) 
  
  def get_num_seeds(self, house_num): 
    return self.game_board[house_num] 
    
  def is_game_won(self): 
    if (self.game_board[1:].count(0) == len(self.game_board[1:])): 
      return True 
    return False 
    
  def is_legal_move(self, house_num): 
    if (house_num == 0): 
      return False 
    elif (self.game_board[house_num] == house_num): 
      return True 
    return False 
    
  def apply_move(self, house_num): 
    if self.is_legal_move(house_num): 
      self.game_board[house_num] = 0 
      for num in range(house_num): 
        self.game_board[num] += 1 
        
  def choose_move(self): 
    for num in self.game_board[1:]: 
      if (self.game_board.index(num, 1) == num): 
        return num 
    return 0 
      
  def plan_moves(self): 
    ret = [] 
    while (not self.is_game_won()): 
      check_num = self.choose_move() 
      if (check_num != 0): 
        ret.append(check_num) 
      if (check_num == 0): 
        break 
      #print str(self), 'moving#' + str(check_num)
      self.apply_move(check_num) 
    #print str(self)
    return ret

solitaire_mancala_test_suite.run_suite(SolitaireMancala)

# suite = poc_simpletest.TestSuite()
# # for case in solitaire_mancala_test_cases.TEST_CASES:
# #   game = SolitaireMancala()
# #   game.set_board(case)
# #   moves = str(game.plan_moves())
# #   message = 'Testing' + str(case) + ': '
# #   expected_result = str(solitaire_mancala_test_cases.EXPECTED_RESULTS[str(case)])
# #   suite.run_test(moves, expected_result, message)
# game = SolitaireMancala()
# suite.run_test(str(game), str([0]), 'Test#100: init Game')
# game.set_board([0, 1])
# suite.run_test(str(game), str([1, 0]), 'Test#200: set_board([0, 1])')
# game.set_board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# suite.run_test(str(game), str([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), 'Test#300: set_board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])')
# suite.run_test(str(game.get_num_seeds(0)), str(0), 'Test#400: get_num_seeds(0)')
# suite.run_test(str(game.get_num_seeds(10)), str(10), 'Test#500: get_num_seeds(10)')
# game.set_board([0, 0, 0, 0])
# suite.run_test(str(game.is_game_won()), str(True), 'Test#600: is_game_won()')
# game.set_board([10, 0, 0, 0, 0])
# suite.run_test(str(game.is_game_won()), str(True), 'Test#700: is_game_won()')
# game.set_board([1, 0, 2, 1, 4, 5, 6])
# suite.run_test(str(game.is_game_won()), str(False), 'Test#800: is_game_won()')
# game.set_board([0, 1, 3, 23, 4])
# suite.run_test(str(game.is_legal_move(0)), str(False), 'Test#900: is_legal_move(0)')
# suite.run_test(str(game.is_legal_move(1)), str(True), 'Test#1000: is_legal_move(1)')
# suite.run_test(str(game.is_legal_move(2)), str(False), 'Test#1100: is_legal_move(2)')
# suite.run_test(str(game.is_legal_move(3)), str(False), 'Test#1200: is_legal_move(3)')
# suite.run_test(str(game.is_legal_move(4)), str(True), 'Test#1300: is_legal_move(4)')
# game.apply_move(4)
# suite.run_test(str(game), str([0, 24, 4, 2, 1]), 'Test#1400: apply_move(4)')
# game.apply_move(2)
# suite.run_test(str(game), str([0, 24, 4, 2, 1]), 'Test#1500: apply_move(2)')
# game.set_board([0, 0, 1, 3, 4, 5, 6])
# suite.run_test(str(game.choose_move()), str(3), 'Test#1600: choose_move()')
# game.set_board([0, 0, 0, 0, 2, 4, 6])
# suite.run_test(str(game.plan_moves()), str([6, 1, 5, 1, 2, 1, 4, 1, 3, 1, 2, 1]), 'Test#1700: plan_moves()')

# suite.report_results()
