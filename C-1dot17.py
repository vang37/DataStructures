#Question:
#
#Had we implemented the scale function (page 25) as follows, does it work properly?
#
#    def scale(data, factor): 
#        for val in data:
#            val *= factor
#
#Explain why or why not.

#Summary
#The "good" scale function changes the data list because it is directly modifying the 
# list's elements, not the numeric values themselves. Lists are mutable, and changes to 
# their elements are visible outside the function due to the list reference being passed 
# around, even if the numeric values themselves are immutable.

#print ('Good scaling')
#def good_scale(data, factor):
#    for j in range(len(data)):
#        data[j] *= factor
#    return data
#
#data = [1,2,3,4,5]; print (data)
#data = good_scale(data, 5); print (data)
#
#print('Bad scaling')
#def scale(data, factor):
#    for val in data:
#        val *= factor
#    return data
#
#data = [1,2,3,4,5]; print (data)
#data = scale(data, 5); print (data)

#The good_scale function iterates over the indices of the data list and multiplies
# each element by "factor." It modifies the data list in place.

#This function will correctly scale each element in the data list by "factor."

#The scale function iterates over the values in the data list, attempting to multiply 
# each value by "factor." However, "val" is a local variable in the loop and does not 
# affect the original list data.

#This function will not scale the elements in the data list. Instead, it will return 
# the original list data unmodified. The "val" variable is just a copy of each element 
# and changing it does not alter the original list.

