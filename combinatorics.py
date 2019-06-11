import math
import fractions


def enums(set_size, output_length):
    '''
    Returns the number of possible enumerations, including duplicates, for
    a given set of size set_size, with an output of size output_length
    '''
    return set_size**output_length


def enums_no_dupes(set_size, output_length):
    '''
    Returns the number of possible enumerations, excluding duplicates, for
    a given set of size set_size, with an outuput of size output_length
    '''
    # Calculated using the formula:
    # (output_length + set_size - 1)! / output_length! * (set_size - 1)!
    return math.factorial(output_length + set_size - 1) / (
        math.factorial(output_length) * math.factorial(set_size - 1))


def perms(set_size, output_length):
    '''
    Returns the number of possible permutations for
    a set of size set_size, with an output size of output_length
    '''
    # Calculated by dividing the factorial of the set_size
    # by the factorial of the output_length
    # (set_size! / output_length!)
    # Since there are terms that cancel out up to (set_size - output_length)
    # instead of using math.factorial(), a loop is used starting
    # @ set_size and striding in reverse to (set_size - output_length)
    num_perms = 1
    for idx in range(set_size, set_size - output_length, -1):
        num_perms *= idx
    return num_perms


def combos(set_size, output_length):
    '''
    Returns the number of possible combinations for
    a set of size set_size, with an output size of output_length
    '''
    # Calculated by dividing the factorial of the set_size
    # by the factorial of the output_length multiplied by
    # the factorial of the set_size
    # set_size! / (output_length! * set_size!)
    num_perms = perms(set_size, output_length)
    return num_perms / math.factorial(output_length)


def subsets(set_size):
    '''
    Returns the number of possible subsets for
    a set of size set_size
    '''
    subset_count = 0
    for length in range(set_size + 1):
        combinations = combos(set_size, length)
        subset_count += combinations
    return subset_count


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


def gen_sorted_sequences(outcomes, length):
    """
    Function that creates all sorted sequences via gen_all_sequences
    """
    all_sequences = gen_all_sequences(outcomes, length)
    sorted_sequences = [tuple(sorted(sequence)) for sequence in all_sequences]
    return set(sorted_sequences)


def gen_permutations(outcomes, length):
    """
    Iterative function that generates set of permutations of
    outcomes of length num_trials
    No repeated outcomes allowed
    """
    ans = set([()])
    # add code here
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                if item in seq:
                    continue
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans


def gen_combinations(outcomes, length):
    '''
    Function that creates all combinations for a given set
    of outcomes at a given length.
    '''
    # get the permutations for the outcomes
    permutations = gen_permutations(outcomes, length)
    # sort the permutations so we can eliminate duplicates
    # (ie ('a', 'b') & ('b', 'a')) since they represent
    # the same combination of values
    sorted_permutations = [
        tuple(sorted(sequence)) for sequence in permutations
    ]
    # eliminate the duplicates by placing the sorted list into a set
    return set(sorted_permutations)


def gen_subsets(outcomes):
    subsets = []
    for length in range(len(outcomes) + 1):
        subsets.append(gen_combinations(outcomes, length))
    return subsets


def pascals_triangle(row, cell):
    '''
    Returns the value of the given cell
    in the given row of Pascal's triangle
    '''
    return math.factorial(row) / (
        math.factorial(cell) * math.factorial(abs(row - cell)))


print combos(6, 2)
print sorted(gen_combinations([1, 2, 3, 4, 5, 6], 2))


# print enums(2, 2)
# sequences = gen_all_sequences([1, 2], 2)
# print 'sequences =', sequences
# print 'len(sequences) =', len(sequences)

# Final example for homework problem

# outcome = set(["a", "b", "c", "d", "e", "f"])

# permutations = gen_permutations(outcome, 4)
# permutation_list = list(permutations)
# permutation_list.sort()
# print permutation_list
# print "Answer is", permutation_list[100]

# outcome = set(['a', 'b', 'c'])
# permutations = gen_permutations(outcome, 3)
# print permutations

# print
# print 'pascals_triangle(row=1, cell=1):', pascals_triangle(1, 1)
# print 'pascals_triangle(row=1, cell=2):', pascals_triangle(1, 2)
# print 'pascals_triangle(row=5, cell=3):', pascals_triangle(5, 3)
# print 'pascals_triangle(row=7, cell=5):', pascals_triangle(7, 5)
# print 'pascals_triangle(row=6, cell=2):', pascals_triangle(6, 2)
# print 'pascals_triangle(row=0, cell=0):', pascals_triangle(0, 0)

# print
# print 'enums(set_size = 5, output_length = 2):', enums(5, 2)
# print 'enums_no_dupes(set_size = 5, output_length = 2):', enums_no_dupes(5, 2)
# print 'perms(set_size = 5, output_length = 2):', perms(5, 2)
# print 'combos(set_size = 5, output_length = 2):', combos(5, 2)
# print
# print 'enums(set_size = 59, output_length = 6)', enums(59, 6)
# print 'enums_no_dupes(set_size = 59, output_length = 6)', enums_no_dupes(59, 6)
# print 'perms(set_size = 59, output_length = 6)', perms(59, 6)
# print 'combos(set_size = 59, output_length = 6)', combos(59, 6)
# print
# outcome = set(["a", "b", "c", "d", "e", "f"])
# permutations = gen_permutations(outcome, 4)
# permutation_list = list(permutations)
# permutation_list.sort()
# print
# print 'Answer is', permutation_list[100]
# print
# outcome = set([1, 2])
# all_sequences = gen_all_sequences(outcome, len(outcome))
# print
# print 'subsets(len(outcome)):', subsets(len(outcome))
# print
# print 'gen_subsets(outcome):', gen_subsets(outcome)
# print
# outcome = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
# suited_5_card_combo_count = combos(len(outcome), 5)
# print 'five card combinations of a given suit:', suited_5_card_combo_count
# outcome = set([1, 2, 3, 4])
# suited_1_card_choice_count = combos(len(outcome), 1)
# print '1 card combination of a given suit', suited_1_card_choice_count
# print 'probability of a flush:', 1 / (float(suited_1_card_choice_count) * suited_5_card_combo_count)
# print
# print
# print
# print subsets(2)