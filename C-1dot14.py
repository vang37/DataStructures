def even(k):
    odds = [1, 3, 5, 7, 9]
    k = str(k)
    return int(k[-1]) not in odds

def get_odd_pair(array):
    first_odd = None
    for num in array:
        if not even(num):
            if num != first_odd and first_odd != None:
                return "Found: ", (first_odd, num)
            else:
                first_odd = num
    return 'None Found'
    
#def has_odd_product_pair(sequence):
#    odd_numbers = set()
#    for number in sequence:
#        if number % 2 != 0:
#            odd_numbers.add(number)
#        if len(odd_numbers) >= 2:
#            return True
#    return False

data = [1,2,3,4,5,6,7,8,9,10]

print(get_odd_pair(data))
