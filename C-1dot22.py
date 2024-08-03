def dot_product(a: list, b: list):
    assert len(a) == len(b), "Lengths of vectors must be equal."
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return c

print(dot_product([1,2],[3,4]))

def real_dot_product(a: list, b: list):
    assert len(a) == len(b), "Lengths of vectors must be equal."
    return sum(x*y for x, y in zip(a, b))

a = [1, 2, 3]
b = [4, 5, 6]
print(real_dot_product(a,b))
