def distinction_test(seq):
    if len(seq) < 2:
        return "This test is unnecessary."
    else:
        i = 1
        l = len(seq)
        for j in range(i, l):
            if seq[i - 1] == seq[j]:
                return False
            else:
                i += 1
        return True

#def are_distinct(sequence):
#    unique_elements = set(sequence)
#    return len(unique_elements) == len(sequence)

data = [1,2,3,4,5,6]; print (distinction_test(data))
data = [1,2,3,3,5,6]; print (distinction_test(data))
data = []; print (distinction_test(data))
