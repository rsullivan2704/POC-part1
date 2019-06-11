"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    return max([value * hand.count(value) for value in hand])


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    ex_value = 0.0
    outcomes = range(1, num_die_sides + 1)
    rolls = gen_all_sequences(outcomes, num_free_dice)
    for roll in rolls:
        tmp_dice = list(held_dice)
        tmp_dice.extend(roll)
        current_score = score(tmp_dice)
        ex_value += current_score
    return ex_value / len(rolls)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    result_set = set()
    for idx in range(len(hand) + 1):
        full_set = set([()])
        for dummy_idx in range(idx):
            partial_set = set()
            for partial_sequence in full_set:
                for item in hand:
                    if item in partial_sequence and \
                        partial_sequence.count(item) >= hand.count(item):
                        continue
                    else:
                        new_sequence = list(partial_sequence)
                        new_sequence.append(item)
                        partial_set.add(tuple(new_sequence))
            full_set = partial_set
        result_set.update(full_set)
    return set([tuple(sorted(sequence)) for sequence in result_set])


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    holds = gen_all_holds(hand)
    best_value = 0.0
    best_hold = None
    for hold in holds:
        free_dice = len(hand) - len(hold)
        current_value = expected_value(hold, num_die_sides, free_dice)
        if current_value > best_value:
            best_value = current_value
            best_hold = hold
    return (best_value, best_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    # print expected_value((5, 5, 6, 6), 6, 1)
    # print expected_value((5, 6, 6), 6, 2)
    # print expected_value((6, 6), 6, 3)
    # print expected_value((5, 6), 6, 3)
    # print expected_value((), 6, 5)
    # print strategy((1, ), 6)
    # print expected_value((2, 2), 6, 2)
    # outcomes = (1, 1, 2)
    # print 'outcomes: ', outcomes

    # limited_seq = set()
    # for idx in range(len(outcomes)):
    #     limited_seq.update(gen_limited_sequences(outcomes, idx))
    # limited_seq.add(outcomes)
    # print 'limited_seq:', sorted(limited_seq)

    # print 'gen_all_holds(hand = (1, 1, 2)):', sorted(gen_all_holds(outcomes))

    # seqs = set()
    # for idx in range(len(outcomes)):
    #     seqs.update(gen_all_sequences(outcomes, idx))
    # seqs.add(outcomes)
    # print 'seqs:', sorted(seqs)

    # sort_seqs = set()
    # for idx in range(len(outcomes)):
    #     sort_seqs.update(gen_sorted_sequences(outcomes, idx))
    # sort_seqs.add(outcomes)
    # print 'sort_seqs:', sorted(sort_seqs)

    # perms = set()
    # for idx in range(len(outcomes)):
    #     perms.update(gen_permutations(outcomes, idx))
    # print 'perms:', sorted(perms)

    # combos = set()
    # for idx in range(len(outcomes)):
    #     combos.update(gen_combinations(outcomes, idx))
    # print 'combos:', sorted(combos)
    # num_die_sides = 6
    # hand = (1, 1, 1, 5, 6)
    # hand_score, hold = strategy(hand, num_die_sides)
    # print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score


# run_example()

# import poc_holds_testsuite
# poc_holds_testsuite.run_suite(gen_all_holds)
