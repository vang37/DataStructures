def vowel_counter(string):
    num = 0
    vowels = "aeiouAEIOU"
    for letter in string:
        if letter in vowels:
            num += 1
    return num

#def count_vowels(s):
#    vowels = "aeiouAEIOU"
#    return sum(1 for char in s if char in vowels)
