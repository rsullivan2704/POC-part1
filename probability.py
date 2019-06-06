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
  calculated to the given selection_count.
  '''
  ex_value = 0
  #if selection_count == 1:
    # The expected value is calculated, when the output length is 1,
    # by multiplying the probability the value will occur by the value
    # itself and adding the products together across all possible values.
  prob = probability(value_set)
  for value in value_set:
    ex_value += (value * prob)
  #else:
    # base_prob = probability(value_set, selection_count)
    # values = cb.gen_sorted_sequences(value_set, selection_count)
    # minimum = selection_count * min(value_set)
    # maximum = selection_count * max(value_set)
    # for value in range(minimum, maximum + 1):
    #   possible_combos = [selections for selections in values if sum(selections) == value]
    #   prob = base_prob * len(possible_combos)
    #   ex_value += (value * prob)
  return ex_value ** selection_count

# value_set = set([1, 2, 3, 4, 5, 6])
# print
# print 'probability(value_set = set([1, 2, 3, 4, 5, 6])):', probability(value_set)
# print 'probability(value_set = set([1, 2, 3, 4, 5, 6]), selection_count = 2):', probability(value_set, 2)
# print 'expected_value(value_set = set([1, 2, 3, 4, 5, 6])):', expected_value(value_set)
# print 'expected_value(value_set = set([1, 2, 3, 4, 5, 6]), selection_count = 2:', expected_value(value_set, 2)
value_set = set([1, 2, 3, 4])
print
print 'expected_value(value_set = set([1, 2, 3, 4])):', expected_value(value_set)
print 'expected_value(value_set = set([1, 2, 3, 4]), selection_count = 4:', expected_value(value_set, 4)
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
deck_set = set([i for i in range(1, 53)])
card_set = set([i for i in range(1, 14)])
suit_set = set([i for i in range(1, 5)])
deck_prob = probability(deck_set, 5)
deck_combos = cb.combos(len(deck_set), 5)
card_prob = probability(card_set, 5)
card_combos = cb.combos(len(card_set), 5)
suit_prob = probability(suit_set, 1)
print 'probability(value_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, ..., 52]), selection_count = 5):', deck_prob
print 'combos(set_size = ' + str(len(deck_set)) + ', output_length = 5):', deck_combos
print 'combos(set_size = ' + str(len(card_set)) + ', output_length = 5):', card_combos
print 'probability of 5 card draw of same suit:', float(card_combos) / (deck_combos * suit_prob)
print 'multiply the number of possible combinations of cards in a deck, by the probability of a suit (2,598,960 * 1/4)'
print 'and divide that into the number of possible combinations of the same suit (1287)'
# value_set = set([])
# for suit in range(1, 5):
#   for value in range(1, 14):
#     value_set.add(('suit: ' + str(suit), 'value: ', str(value)))
# card_prob = probability(value_set, 5)
# value_set = set([])
# for suit in range(1, 5):
#   value_set.add(suit)
# suit_prob = probability(value_set, 5)
# value_set = set([])
# for value in range(1, 14):
#   value_set.add(value)
# value_prob = probability(value_set, 5)
# print 'suit probability:', suit_prob
# print 'value probability:', value_prob
# print 'card probability:', card_prob
# five_card_suit_prob = suit_prob * value_prob
# print 'five cards of a suit probability:', five_card_suit_prob