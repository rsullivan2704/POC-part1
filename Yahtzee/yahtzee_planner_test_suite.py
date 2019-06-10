import poc_simpletest
import yahtzee_planner


def run_suite(yahtzee_imp):
    '''
  Testing suite for yahtzee planner implementation
  '''

    # create the TestSuite object
    suite = poc_simpletest.TestSuite()
    suite.run_test(
        yahtzee_imp.gen_all_sequences(set([1, 2, 3]), 3),
        set([(1, 3, 2), (1, 3, 1), (3, 3, 1), (2, 3, 1), (3, 3, 3), (2, 3, 2),
             (3, 3, 2), (2, 3, 3), (3, 2, 2), (3, 1, 3), (3, 2, 3), (3, 1, 2),
             (1, 2, 1), (3, 1, 1), (3, 2, 1), (1, 2, 2), (1, 2, 3), (1, 1, 1),
             (2, 1, 2), (2, 2, 3), (2, 1, 3), (2, 2, 2), (2, 2, 1), (2, 1, 1),
             (1, 1, 2), (1, 1, 3), (1, 3, 3)]),
        'Test#1: gen_all_sequences(outcomes = set([1, 2, 3]), length = 3)')

    suite.run_test(yahtzee_imp.gen_all_holds((1, 1, 2)),
                   set([(), (1, ), (1, 1), (1, 1, 2), (1, 2), (2, )]),
                   'Test#2: gen_all_holds(hand = (1, 1, 2)')

    suite.run_test(
        yahtzee_imp.gen_all_holds((3, 1, 2)),
        set([(), (1, ), (1, 2), (1, 3), (3, 1, 2), (2, ), (2, 3), (3, )]),
        'Test#3: gen_all_holds(hand = (1, 1, 2)')

    suite.run_test(
        sorted(yahtzee_imp.gen_all_holds((1, 1, 1, 5, 6))),
        sorted(
            set([(), (1, ), (1, 1), (1, 5), (1, 5, 6), (1, 6), (1, 1, 1),
                 (1, 1, 5), (1, 1, 6), (1, 1, 5, 6), (1, 1, 1, 5),
                 (1, 1, 1, 6), (1, 1, 1, 5, 6), (5, ), (5, 6), (6, )])), '')

    suite.run_test(yahtzee_imp.score([6, 1, 1, 2, 3]), 6,
                   'Test#5: score(hand = [6, 1, 1, 2, 3])')

    suite.run_test(yahtzee_imp.score([1, 1, 1, 2, 4]), 4,
                   'Test#6: score(hand = [1, 1, 1, 2, 4])')

    suite.run_test(yahtzee_imp.score([1, 1, 1, 2, 3]), 3,
                   'Test#7: score(hand = [1, 1, 1, 2, 3])')

    suite.run_test(
        round(yahtzee_imp.expected_value((), 6, 5), 8),
        round(3.5, 8),
        'Test#8: expected_value(held_dice = (), num_die_sides = 6, num_free_dice = 5)'
    )

    suite.run_test(
        round(yahtzee_imp.expected_value((1, 1, 1), 6, 2), 8),
        round(5.61904761905, 8),
        'Test#8: expected_value(held_dice = (1, 1, 1), num_die_sides = 6, num_free_dice = 2)'
    )

    suite.run_test(
        round(yahtzee_imp.expected_value((5, ), 6, 4), 8),
        round(10.5079365079, 8),
        'Test#9: expected_value(held_dice = (5), num_die_sides = 6, num_free_dice = 4)'
    )

    suite.run_test(
        round(yahtzee_imp.expected_value((6, ), 6, 4), 8),
        round(11.3095238095, 8),
        'Test#10: expected_value(held_dice = (6), num_die_sides = 6, num_free_dice = 4)'
    )

    suite.run_test(
        round(yahtzee_imp.expected_value((2, 2), 6, 2), 8),
        round(5.83333333333, 8),
        'Test#10: expected_value(held_dice = (2, 2), num_die_sides = 6, num_free_dice = 2)'
    )

    strat = yahtzee_imp.strategy((1, ), 6)

    suite.run_test((round(strat[0], 8), strat[1]),
                   (round(3.5, 8), ()),
                   'Test#11: strategy(held_dice = (1, ), num_die_sides = 6)')

    suite.report_results()


run_suite(yahtzee_planner)
