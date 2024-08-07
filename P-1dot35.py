import random 

def distinct(sequence):
    unique_elements = set(sequence)
    return len(unique_elements) == len(sequence)

def date_check(num):
    date_pool = [random.randint(1, 366) for i in range(num)]
    if not distinct(date_pool): 
        return True
    return False

def main():
    i = 0
    for _ in range(number_of_rooms):
        if date_check(number_of_people):
            i += 1
    return "n = {}: ".format(number_of_people), "%: ",  i/number_of_rooms
            
for number_of_people in [5,10,15,20,21,22,23,24,25,30,40,50,75,100]:
    number_of_rooms = 1000000
    print(main())
