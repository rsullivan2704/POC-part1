"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""

class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._board = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._board = configuration[0:]
    
    def __str__(self):
      """
      Return string representation for Mancala board
      """
      return str(self._board[::-1])
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        return len([seed for seed in self._board[1:] if seed > 0]) == 0
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        return 0 < house_num < len(self._board) and self._board[house_num] == house_num
    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            self._board[house_num] = 0
            for house in range(house_num):
                self._board[house] += 1
            # next_house = house_num - 1
            # while next_house >= 0:
            #     self._board[next_house] += 1
            #     next_house -= 1

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        legal_moves = [house for house, seeds in enumerate(self._board) if house > 0 and self.is_legal_move(house)]
        return legal_moves[0] if len(legal_moves) > 0 else 0

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        # copy the board so it can be reset after planning
        board = self._board[0:]
        moves = []
        next_move = self.choose_move()
        while next_move != 0:
          #print str(self), 'moving#' + str(next_move)
          self.apply_move(next_move)
          moves.append(next_move)
          next_move = self.choose_move()
        #print str(self)
        self.set_board(board)
        return moves

import solitaire_mancala_test_suite

solitaire_mancala_test_suite.run_suite(SolitaireMancala)

# import poc_simpletest
# import solitaire_mancala_test_cases
# suite = poc_simpletest.TestSuite()
# for case in solitaire_mancala_test_cases.TEST_CASES:
#   game = SolitaireMancala()
#   game.set_board(case)
#   moves = str(game.plan_moves())
#   message = 'Testing' + str(case) + ': '
#   expected_result = str(solitaire_mancala_test_cases.EXPECTED_RESULTS[str(case)])
#   suite.run_test(moves, expected_result, message)
# suite.report_results()


# Create tests to check the correctness of your code

# def test_mancala():
#     """
#     Test code for Solitaire Mancala
#     """
    
    # my_game = SolitaireMancala()
    # print "Testing init - Computed:", my_game, "Expected: [0]"
    
    # config = [0, 0, 1, 1, 3, 5, 0]    
    # my_game.set_board(config)       
    # print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    # print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config[1]
    # print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config[3]
    # print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config[5]

    # add more tests here
    # config = [0,0,0,0,0,0,0]
    # my_game.set_board(config)
    # print "Testing set_board - Computed:", str(my_game), "Expected:", str([0,0,0,0,0,0,0,0])
    # print 'Testing is_game_won - Computed:', my_game.is_game_won(), 'Expected:', True

    # config = [0,0,0,1,0,0]
    # my_game.set_board(config)
    # print "Testing set_board - Computed:", str(my_game), "Expected:", str([0,0,1,0,0,0,0])
    # print 'Testing is_game_won - Computed:', my_game.is_game_won(), 'Expected:', False

    # config = [0,2,0,2,0,0,0]
    # my_game.set_board(config)
    # print "Testing set_board - Computed:", str(my_game), "Expected:", str([0,0,0,2,0,2,0,0])
    # print 'Testing is_legal_move - Computed:', my_game.is_legal_move(2), 'Expected:', True
    # print 'Testing is_legal_move - Computed:', my_game.is_legal_move(4), 'Expected:', False
    # my_game.apply_move(2)
    # print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0,0,0,2,0,0,1,1])
    # my_game.set_board(config)
    # print "Testing set_board - Computed:", str(my_game), "Expected:", str([0,0,0,2,0,2,0,0])
    # print 'Testing choose_move - Computed:', str(my_game.choose_move()), 'Expected:', str(2)

    # config = [0,1,0,2,0,0,0]
    # my_game.set_board(config)
    # print "Testing set_board - Computed:", str(my_game), "Expected:", str([0,0,0,2,0,1,0,0])
    # print 'Testing choose_move - Computed:', str(my_game.choose_move()), 'Expected:', str(0)

    # config = [0,2,0,4,0,0,0]
    # my_game.set_board(config)
    # print "Testing set_board - Computed:", str(my_game), "Expected:", str([0,0,0,4,0,2,0,0])
    # print 'Testing choose_move - Computed:', str(my_game.choose_move()), 'Expected:', str(2)

    # config = [0,1,0,4,0,0,0]
    # my_game.set_board(config)
    # print "Testing set_board - Computed:", str(my_game), "Expected:", str([0,0,0,4,0,1,0,0])
    # print 'Testing choose_move - Computed:', str(my_game.choose_move()), 'Expected:', str(4)

    # config = [0,2,0,4,0,0,0]
    # my_game.set_board(config)
    # print "Testing set_board - Computed:", str(my_game), "Expected:", str([0,0,0,4,0,2,0,0])
    # print 'Testing plan_moves - Computed:', str(my_game.plan_moves()), 'Expected:', str([2,1,4,1])
    
# test_mancala()

# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())
