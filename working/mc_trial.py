import random

def roll_die():
  return random.randint(1, 4)

def trial():
  results = []
  for idx in range(10):
    die1 = roll_die()
    die2 = roll_die()
    results.append(die1 * die2)
  # for result in results:
  #   print result
  # print 'sum:', sum(results)
  return results

trials = trial()

print 'expected value:', float(sum(trials)) / len(trials)
