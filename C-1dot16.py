#Question:
#
#In our implementation of the "scale" function (page25), the body of the loop 
# executes the command data[j] = factor. We have discussed that numeric types are immutable,
# and that use of the "=" operator in this context causes the creation of a new instance 
# (not the mutation of an existing instance). How is it still possible, then, that our 
# implementation of scale changes the actual parameter sent by the caller?

#Key Points:
#
#Numeric Immutability:
# Numeric types in Python (e.g., integers and floats) are immutable, meaning that 
# operations that modify their value actually create a new instance rather than changing 
# the original instance.
#
#Mutability of Lists:
# Lists (or more generally, mutable objects) in Python can be modified in place. 
# When you use indexing to access an element of a list, you’re working directly with 
# the element at that position in memory.
#
#How the "good" scale function works:
# "data[j] *= factor" is an in-place operation that changes the value of data[j] in the 
# original data list. Even though data[j] itself is immutable, the data list is mutable. 
# The *= operator modifies the value of data[j] directly within the list.
# When data[j] *= factor is executed, Python calculates the new value 
# (which is data[j] * factor) and then assigns this new value to data[j]. The data list i
# still refers to the same list object in memory, and now its contents have been updated.
#
#Why the Changes Are Reflected:
# List Reference: When you pass data to the good_scale function, you are passing a reference 
# to the original list, not a copy. Therefore, any modification made to data inside the 
# function will be reflected outside the function as well. Element Modification: Even though 
# numeric values themselves are immutable, the data list itself is mutable, allowing in-place 
# updates to its elements.
#
#Summary
# The "good" scale function changes the data list because it is directly modifying the list's 
# elements, not the numeric values themselves. Lists are mutable, and changes to their 
# elements are visible outside the function due to the list reference being passed around, 
# even if the numeric values themselves are immutable.


