def list_reverse(l):
    lngth = len(l)
    reverse_l = [None for _ in range(lngth)]
    for i in range(lngth):
        k = -i - 1
        reverse_l[k] = l[i]
    return reverse_l

#def reverse_list(l):
#    start_index = 0
#    end_index = len(l) - 1
#    while start_index < end_index:
#        # Swap elements
#        l[start_index], l[end_index] = l[end_index], l[start_index]
#        # Move indices towards the center
#        start_index += 1
#        end_index -= 1
#    return l

print([5, 4, 7, 6, 3, 4, 8, 7, 5, 3, 2])
print(list_reverse([2, 3, 5, 7, 8, 4, 3, 6, 7, 4, 5]))
