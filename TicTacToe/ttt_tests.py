import poc_simpletest as test
import poc_ttt_provided as provided
import ttt

board = provided.TTTBoard(3, False, None)

def run_suite():
    suite = test.TestSuite()
    ttt.mc_trial(board, provided.PLAYERO)
    print board
    suite.run_test(board, '', 'Board Test')

if __name__ == '__main__':
    run_suite()