#Question:
#
#In our implementation of the "scale" function (page25), the body of the loop 
# executes the command data[j] *= factor. We have discussed that numeric types are immutable,
# and that use of the "*=" operator in this context causes the creation of a new instance 
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

