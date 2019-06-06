from POC_PART1 import poc_simpletest
import simple_dice

def run_suite():
  '''
  Testing suite for simple dice game implementation
  '''

  # create the TestSuite object
  suite = poc_simpletest.TestSuite()
  suite.run_test(simple_dice.gen_all_sequences(set([1, 2, 3]), 3), set([(1, 3, 2), (1, 3, 1), (3, 3, 1), (2, 3, 1), (3, 3, 3), (2, 3, 2), (3, 3, 2), (2, 3, 3), (3, 2, 2), (3, 1, 3), (3, 2, 3), (3, 1, 2), (1, 2, 1), (3, 1, 1), (3, 2, 1), (1, 2, 2), (1, 2, 3), (1, 1, 1), (2, 1, 2), (2, 2, 3), (2, 1, 3), (2, 2, 2), (2, 2, 1), (2, 1, 1), (1, 1, 2), (1, 1, 3), (1, 3, 3)]), 'Test#1: gen_all_sequences(outcomes = set([1, 2, 3]), length = 3)')
  suite.run_test(simple_dice.max_repeats(()), 0, 'Test#2: max_repeats(())')
  suite.run_test(simple_dice.max_repeats((3, 1, 2)), 1, 'Test#3: max_repeats((3, 1, 2))')
  suite.run_test(simple_dice.max_repeats((3, 3, 2)), 2, 'Test#4: max_repeats((3, 3, 2))')
  suite.run_test(simple_dice.max_repeats((3, 2, 3)), 2, 'Test#4: max_repeats((3, 3, 2))')
  suite.run_test(simple_dice.max_repeats((3, 3, 3)), 3, 'Test#5: max_repeats((3, 3, 3))')
  
  suite.run_test(simple_dice.gen_all_sequences(set([1, 2]), 2), set([(1, 2), (1, 1), (2, 1), (2, 2)]), 'Test#1: gen_all_sequences(outcomes = set([1, 2]), length = 2)')
  suite.run_test(simple_dice.max_repeats(()), 0, 'Test#2: max_repeats(())')
  suite.run_test(simple_dice.max_repeats((1, 2)), 1, 'Test#3: max_repeats((1, 2))')
  suite.run_test(simple_dice.max_repeats((2, 2)), 2, 'Test#4: max_repeats((2, 2))')
  suite.run_test(simple_dice.compute_expected_value(), None, 'Test#5: compute_expected_value() ** Not Fully Implemented **')
  suite.report_results()

run_suite()