def punc_replace(input_string):
    punc = "\"\\!@#$%^&*()_+-=~`{}|[];':<>?,./"
    string = ""
    for char in input_string:
        if char not in punc:
            string += char
    return string

#def punc_replace(input_string):
#    punc = "\"\\!@#$%^&*()_+-=~`{}|[];':<>?,./"
#    return ''.join(char for char in input_string if char not in punc)

print(punc_replace("Let's try, Mike."))
