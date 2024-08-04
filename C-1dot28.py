def norm(v: list, p = 2):
    return (sum((vec)**(p) for vec in v))**(1/p) 

print(norm([4,3]))
print(norm([4,3,4,5], 3))
