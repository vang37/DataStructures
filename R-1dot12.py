import random

def minmax(data):
    if len(data) == 0:
        return
    big = small = data[0]
    for d in data[1:]:
        if d > big:
            big = d
        if d < small:
            small = d
    return (small, big)


def randomchoice(data):
    return random.randrange(minmax(data)[0], minmax(data)[1])
    #index = random.randrange(len(data))
    #return data[index]
    
    #print(choice([2,3,5,7,8,4,3,6,7,4,5]))
data = [2,3,5,7,8,4,3,6,7,4,5]
for _ in range(400):
    print(randomchoice(data), end = ' ')
