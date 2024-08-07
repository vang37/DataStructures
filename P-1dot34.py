import random

def lowercase_alphabet(startIdx, lngth):
    return [chr(i) for i in range(startIdx, startIdx + lngth)]

#lower_alpha = lowercase_alphabet(97, 26)
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
    sent = sent.replace(str(lettr), '')
    rando = random.randint(1, len(sent) - 2)
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
            if letter  == 'I':
                print("ERROR I: ", n)
                sentence = sentence[:random_num] + "i" + sentence[random_num + 1:]
                print(sentence)
            elif sentence[random_num].isspace():
                print("ERROR SPACE: ", n)
                sentence = sentence[:random_num] + "" + sentence[random_num + 1:]
                print(sentence)
            elif letter in lower_alpha:
                print("ERROR LETTER: ", n)
                sentence = sentence[:random_num] + find_unique_replacement(sentence, letter) + sentence[random_num + 1:]
                print(sentence)
            else:
                print("ERROR EOS: ", n)
                sentence = sentence[:random_num] + "!"
                print(sentence)
        else:
            print(sentence)

blackboard(100)
