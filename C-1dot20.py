import random

def shuffle(data):
    lngth = len(data)
    seen = []
    while len(seen) < lngth:
        random_idx = random.randint(0, lngth - 1)
        if random_idx not in seen:
            seen.append(random_idx)
    return [data[x] for x in seen]

#def FY_Shuffle(data):
#    n = len(data)
#    # Perform the Fisher-Yates shuffle algorithm
#    for i in range(n - 1, 0, -1):
#        j = random.randint(0, i)
#        data[i], data[j] = data[j], data[i]
#    return data

data = [1,2,3,4,5,6]
print(shuffle(data))
#print(FY_Shuffle(data))
