import math

def enums(set_size, output_length):
    '''
    Returns the number of possible enumerations, including duplicates, for
    a given set of size set_size, with an output of size output_length
    '''
    return set_size ** output_length

def enums_no_dupes(set_size, output_length):
    '''
    Returns the number of possible enumerations, excluding duplicates, for
    a given set of size set_size, with an outuput of size output_length
    '''
    # Calculated using the formula:
    # (output_length + set_size - 1)! / output_length! * (set_size - 1)!
    return math.factorial(output_length + set_size - 1) / (math.factorial(output_length) * math.factorial(set_size - 1))

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

print
print 'enums(set_size = 5, output_length = 2):', enums(5, 2)
print 'enums_no_dupes(set_size = 5, output_length = 2):', enums_no_dupes(5, 2)
print 'perms(set_size = 5, output_length = 2):', perms(5, 2)
print 'combos(set_size = 5, output_length = 2):', combos(5, 2)
print
print 'enums(set_size = 59, output_length = 6)', enums(59, 6)
print 'enums_no_dupes(set_size = 59, output_length = 6)', enums_no_dupes(59, 6)
print 'perms(set_size = 59, output_length = 6)', perms(59, 6)
print 'combos(set_size = 59, output_length = 6)', combos(59, 6)
print