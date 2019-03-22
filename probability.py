import combinatorics as cb

def probability(value_set, selection_count=1):
  '''
  Given a set of values (value_set), and the optional
  selection_count, return the probability that a value will
  be selected at random, assuming fair selection.
  '''
  if selection_count == 1:
    return 1.0 / len(value_set)
  else:
    return probability(value_set) ** selection_count

def expected_value(value_set, selection_count=1):
  '''
  Return the expected value to be returned on any
  random selection from the value_set supplied optionally
  calculated to the given input_length.
  '''
  ex_value = 0
  if selection_count == 1:
    # The expected value is calculated, when the output length is 1,
    # by multiplying the probability the value will occur by the value
    # itself and adding the products together across all possible values.
    prob = probability(value_set)
    for value in value_set:
      ex_value += (value * prob)
  else:
    base_prob = probability(value_set, selection_count)
    values = cb.gen_sorted_sequences(value_set, selection_count)
    minimum = selection_count * min(value_set)
    maximum = selection_count * max(value_set)
    for value in range(minimum, maximum + 1):
      possible_combos = [selections for selections in values if sum(selections) == value]
      prob = base_prob * len(possible_combos)
      ex_value += (value * prob)
  return ex_value


value_set = set([1, 2, 3, 4, 5, 6])
print
print 'probability(value_set = set([1, 2, 3, 4, 5, 6])):', probability(value_set)
print 'probability(value_set = set([1, 2, 3, 4, 5, 6]), selection_count = 2):', probability(value_set, 2)
print 'expected_value(value_set = set([1, 2, 3, 4, 5, 6])):', expected_value(value_set)
print 'expected_value(value_set = set([1, 2, 3, 4, 5, 6]), selection_count = 2:', expected_value(value_set, 2)
value_set = set([1, 2, 3, 4])
print
print 'expected_value(value_set = set([1, 2, 3, 4])):', expected_value(value_set)
print 'expected_value(value_set = set([1, 2, 3, 4]), selection_count = 2:', expected_value(value_set, 2)
print
value_set = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print
print 'enums(set_size = len(value_set), output_length = 5):', cb.enums(len(value_set), 5)
print 'perms(set_size = len(value_set), output_length = 5):', cb.perms(len(value_set), 5)
print 'probability(value_set = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])):', probability(value_set)
print 'probability(value_set = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), selection_count = 5):', probability(value_set, 5)
print 'expected_value(value_set = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])):', expected_value(value_set)
print 'expected_value(value_set = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), selection_count = 5:', expected_value(value_set, 5)
print