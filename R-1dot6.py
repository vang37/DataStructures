def is_even(k: int):
    assert type(k) == int, "Input must be an integer."
    return (k & 1) == 0

def sumoddsquares(n):
    if n != int(n) or n != abs(n):
        return
    return sum(i**2 for i in range(1, n) if not is_even(i))
    
print(sumoddsquares(2))
print(sumoddsquares(10))
print(sumoddsquares(0))
print(sumoddsquares(4))
print(sumoddsquares(-5))
