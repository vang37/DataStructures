def distinction_test(seq):
    return len(seq) == len(set(seq))

def map_to_letters(num_string):
    assert len(num_string) == 6, "This is not going to work, CATDOG!"
    for i in range(len(num_string)):
        if num_string[i] == '1':
            num_string = num_string.replace('1', 'c')
        if num_string[i] == '2':
            num_string = num_string.replace('2', 'a')
        if num_string[i] == '3':
            num_string = num_string.replace('3', 't')
        if num_string[i] == '4':
            num_string = num_string.replace('4', 'd')
        if num_string[i] == '5':
            num_string = num_string.replace('5', 'o')
        if num_string[i] == '6':
            num_string = num_string.replace('6', 'g')
    return num_string

def letter_permutations():
    s = []
    num_chars = ['0', '7', '8', '9']
    for x in range(100000, 1000000):
        x = str(x)
        if distinction_test(x) and  all(char not in x for char in num_chars):
            s.append(map_to_letters(x))
    return s

perms = letter_permutations()

for p in perms:
    print(p)

#def distinction_test(seq):
#    """Check if all characters in the sequence are unique."""
#    return len(seq) == len(set(seq))
#
#def map_to_letters(num_string):
#    """Map numeric string to corresponding letters."""
#    # Define a mapping dictionary
#    mapping = {
#        '1': 'c',
#        '2': 'a',
#        '3': 't',
#        '4': 'd',
#        '5': 'o',
#        '6': 'g'
#    }
#    # Replace each character based on the mapping
#    return ''.join(mapping.get(char, char) for char in num_string)
#
#def letter_permutations():
#    """Generate letter permutations for valid numeric strings."""
#    s = []
#    num_chars = {'0', '7', '8', '9'}  # Set for faster membership checking
#    for x in range(100000, 1000000):
#        x_str = str(x)
#        if distinction_test(x_str) and not any(char in x_str for char in num_chars):
#            s.append(map_to_letters(x_str))
#    return s
#
## Example usage
#result = letter_permutations()
#print(result)  # Output will be a list of letter mappings for valid numeric strings

