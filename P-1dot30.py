import sys

a = int(sys.argv[1])

def cut_by_two(num: int):
    assert num > 2, "Input must be an integer greater than two."
    val = 0
    while num > 2:
        num /= 2
        val += 1

    return val

print(cut_by_two(a))    
