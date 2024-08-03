def sumsquares(n):
    if n != int(n) or n != abs(n):
        return
    #    squares = 0
    #    for i in range(n):
    #        n -= 1
    #        squares += n**2
    #return squares
    return sum(i**2 for i in range(1, n))

print(sumsquares(2))
print(sumsquares(10))
print(sumsquares(0))
print(sumsquares(-5))
