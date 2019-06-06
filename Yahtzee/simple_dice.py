"""
Analyzing a simple dice game
"""

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """
    
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

# example for digits

def max_repeats(seq):
    """
    Compute the maxium number of times that an outcome is repeated
    in a sequence
    """
    counts = [seq.count(value) for value in seq]
    return max(counts) if len(counts) > 0 else 0

def compute_expected_value():
    """
    Function to compute expected value of simple dice game
    """
    ex_value = 0
    outcomes = set([1, 2, 3, 4, 5, 6])
    sequences = gen_all_sequences(outcomes, 3)
    prob = (1 / float(len(sequences)))
    for value in sequences:
      if max_repeats(value) == 1:
        ex_value += -10 * prob
      elif max_repeats(value) == 2:
        ex_value += 10 * prob
      else:
        ex_value += 200 * prob
    #ex_value *= prob
    # singles = [value for value in sequences if max_repeats(value) == 1]
    # doubles = [value for value in sequences if max_repeats(value) == 2]
    # triples = [value for value in sequences if max_repeats(value) == 3]
    # single_prob = float(len(singles)) / len(sequences)
    # double_prob = float(len(doubles)) / len(sequences)
    # triple_prob = float(len(triples)) / len(sequences)
    # single_value = (-10 * len(singles))
    # double_value = (10 * len(doubles))
    # triple_value = (200 * len(triples))
    # ex_value = (single_value + double_value + triple_value) / len(sequences)
    return ex_value

def run_test():
    """
    Testing code, note that the initial cost of playing the game
    has been subtracted
    """
    outcomes = set([1, 2, 3, 4, 5, 6])
    print "All possible sequences of three dice are"
    print gen_all_sequences(outcomes, 3)
    print
    print "Test for max repeats"
    print "Max repeat for (3, 1, 2) is", max_repeats((3, 1, 2))
    print "Max repeat for (3, 3, 2) is", max_repeats((3, 3, 2))
    print "Max repeat for (3, 3, 3) is", max_repeats((3, 3, 3))
    print
    print "Ignoring the initial $10, the expected value was $", compute_expected_value()
    
#run_test()
