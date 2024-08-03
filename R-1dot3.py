def minmax(data):
    if len(data) == 0:
        print("Data source is empty!")
        return
    big = small = data[0]
    for d in data[1:]:
        if d > big:
            big = d
        if d < small:
            small = d
    return (small, big)

print(minmax([1,2,3,4,5,6]))
print(minmax([4,2,5,4,5,6]))
print(minmax([]))
print(minmax([2,35,6]))

