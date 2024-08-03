def even(k):
    odds = [1, 3, 5, 7, 9]
    k = str(k)
    return int(k[-1]) not in odds
    
def is_even(k: int):
    assert type(k) == int, "Input must be an integer."
    return (k & 1) == 0
    
### Explanation
##1. **Bitwise AND Operation:**
#     - k & 1: The bitwise AND operation between k and 1 isolates the least significant bit of k.
#     - If the least significant bit is 0, the result will be 0, indicating k is even.
#     - If the least significant bit is 1, the result will be 1, indicating k is odd.
#
##2. **Comparison:**
#     - (k & 1) == 0: This expression evaluates to True if k is even and False if k is odd.
#    Why It Works
#     - In binary, even numbers end in 0 (e.g., 0000, 0010, 0100), and odd numbers end in 1 (e.g., 0001, 0011, 0101).
#     - By performing a bitwise AND with 1, you effectively check the least significant bit of the number.
#     This method is efficient and adheres to the constraint of not using multiplication, modulo, or division operators.

print(even(2))
print(even(1))
print(even(0))
print(even(100002343))

print(is_even(2))
print(is_even(1))
print(is_even(0))
print(is_even(100002343))
