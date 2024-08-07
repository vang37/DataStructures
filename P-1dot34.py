import random

lower_alpha = set(list('I will never spam my friends again.'))

def random_indices(num, max_range):
    while True:
        test_list = [random.randint(0, max_range - 1) for _ in range(num)]
        if are_distinct(test_list):
            return test_list

def are_distinct(sequence):
    unique_elements = set(sequence)
    return len(unique_elements) == len(sequence)

def find_unique_replacement(sent, lettr):
    sent = list(set(sent.replace(str(lettr), '').replace(' ', '').replace('.', '').replace('I', '')))
    rando = random.randint(0, len(sent) - 1)
    char = sent[rando]
    if char.isspace():
        return ''
    return str(sent[rando])

def blackboard(num_rpt):
    lst = sorted(random_indices(8, 100)) + [num_rpt]
    t = 0
    for n in range(num_rpt):
        sentence = 'I will never spam my friends again.'
        random_num = random.randint(0, len(sentence) - 1)
        random_letter = random.randint(0, 25)
        letter = sentence[random_num]
        if str(n) == str(lst[t]):
            t += 1
            if letter == 'I':
                print("ERROR I: ", n + 1)
                sentence = sentence[:random_num] + "i" + sentence[random_num + 1:]
                print('{}. '.format(n + 1), sentence)
            elif sentence[random_num].isspace():
                print("ERROR SPACE: ", n + 1)
                sentence = sentence[:random_num] + "" + sentence[random_num + 1:]
                print('{}. '.format(n + 1), sentence)
            elif letter in lower_alpha:
                print("ERROR LETTER: ", n + 1)
                sentence = sentence[:random_num] + find_unique_replacement(sentence, letter) + sentence[random_num + 1:]
                print('{}. '.format(n + 1), sentence)
            elif letter == '.':
                print("ERROR EOS: ", n + 1)
                sentence = sentence[:random_num] + "!"
                print('{}. '.format(n + 1), sentence)
        else:
            print('{}. '.format(n + 1), sentence)

blackboard(100)
