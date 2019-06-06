import poc_simpletest
import random
import solitaire_mancala_reference_implementation as reference

def run_suite(game_class):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite() 

    # test the initial configuration of the board using the str method
    test_count = random.randint(100, 1000)
    house_value = 0
    for test_number in range(test_count):   
      # create a game
      game = game_class()
      # create the reference implementation
      ref_imp = reference.SolitaireMancala()
      # initialize a random board
      board_config = [0]
      board_size = random.randint(1, 9)
      for house in range(board_size):
        board_config.append(random.randint(0,10))
      # configure both implementations
      game.set_board(board_config)
      ref_imp.set_board(board_config)
      # test the board against both the erroneous and reference implementations
      suite.run_test(game.plan_moves(), ref_imp.plan_moves(), 'Test#' + str(test_number) + ': ' + str(board_config))

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
    # game.apply_move(game.choose_move())
    # suite.run_test(str(game.choose_move()), str(1), 'Test#1601: choose_move()')
    # game.set_board([0, 0, 0, 0, 2, 4, 6])
    # suite.run_test(str(game.plan_moves()), str([6, 1, 5, 1, 2, 1, 4, 1, 3, 1, 2, 1]), 'Test#1700: plan_moves()')

    # suite.run_test(str(game), str([0]), "Test #0: init")
    # config = [0, 0, 1, 1, 3, 5, 0] 
    # game.set_board(config)
    # suite.run_test(str(game), str([0, 5, 3, 1, 1, 0, 0]), 'Test #1: set_board')
    # suite.run_test(game.get_num_seeds(1), config[1], 'Test #2: get_num_seeds(1)')
    # suite.run_test(game.get_num_seeds(3), config[3], 'Test #2: get_num_seeds(3)')
    # suite.run_test(game.get_num_seeds(5), config[5], 'Test #2: get_num_seeds(5)')
    
    # config = [17, 0, 0, 0, 0, 0, 0]
    # game.set_board(config)
    # suite.run_test(str(game), str([0, 0, 0, 0, 0, 0, 17]), 'Test #4: set_board')
    # suite.run_test(game.is_game_won(), True, 'Test #5: is_game_won')
    
    # config = [17, 0, 0, 1, 0, 0, 0]
    # game.set_board(config)
    # suite.run_test(str(game), str([0, 0, 0, 1, 0, 0, 17]), 'Test #6: set_board')
    # suite.run_test(game.is_game_won(), False, 'Test #7: is_game_won')

    # config = [0, 0, 2, 0, 2, 0, 0]
    # game.set_board(config)
    # suite.run_test(str(game), str([0, 0, 2, 0, 2, 0, 0]), 'Test #8: set_board')
    # suite.run_test(game.is_legal_move(2), True, 'Test #9: is_legal_move(2)')
    # suite.run_test(game.is_legal_move(4), False, 'Test #10: is_legal_move(4)')
    # game.apply_move(2)
    # suite.run_test(str(game), str([0, 0, 2, 0, 0, 1, 1]), 'Test #11: apply_move(2)')
    # game.set_board(config)
    # suite.run_test(str(game), str([0, 0, 2, 0, 2, 0, 0]), 'Test #12: set_board')
    # suite.run_test(str(game.choose_move()), str(2), 'Test #13: choose_move')

    # config = [0, 0, 1, 0, 2, 0, 0]
    # game.set_board(config)
    # suite.run_test(str(game), str([0, 0, 2, 0, 1, 0, 0]), 'Test #14: set_board')
    # suite.run_test(str(game.choose_move()), str(0), 'Test #15: choose_move')

    # config = [0, 0, 2, 0, 4, 0, 0]
    # game.set_board(config)
    # suite.run_test(str(game), str([0, 0, 4, 0, 2, 0, 0]), 'Test #16: set_board')
    # suite.run_test(str(game.choose_move()), str(2), 'Test #17: choose_move')
    # game.apply_move(game.choose_move())
    # suite.run_test(str(game), str([0, 0, 4, 0, 0, 1, 1]), 'Test #18: apply_move(2)')
    # suite.run_test(str(game.choose_move()), str(1), 'Test #19: choose_move')
    # game.apply_move(game.choose_move())
    # suite.run_test(str(game), str([0, 0, 4, 0, 0, 0, 2]), 'Test #19: apply_move(1)')
    # suite.run_test(str(game.choose_move()), str(4), 'Test #20: choose_move')

    # config = [0, 0, 2, 0, 4, 0, 0]
    # game.set_board(config)
    # suite.run_test(str(game), str([0, 0, 4, 0, 2, 0, 0]), 'Test #21: set_board')
    # suite.run_test(str(game.plan_moves()), str([2, 1, 4, 1]), 'Test #22: plan_moves')

    
    # # report number of tests and failures
    suite.report_results()