class Vector:
#Represent a vector in a multidimensional space.
    def __init__(self, *d):
#Create d-dimensional vector of zeros.
        self._coords = [i for i in d] 
    def __len__(self):
#Return the dimension of the vector. 
        return len(self._coords)
    def __getitem__(self, j):
#Return jth coordinate of vector.””” 
        return self._coords[j]
    def __setitem__(self, j, val):
#Set jth coordinate of vector to given value. 
        self._coords[j] = val
    def __add__(self, other):
#Return sum of two vectors.
        if len(self) != len(other): # relies on len method
            raise ValueError( "dimensions must agree" )
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j] 
        return result
    def __sub__(self, other):
#Return difference of two vectors.
        if len(self) != len(other): # relies on len method
            raise ValueError( "dimensions must agree" )
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j] 
        return result
    def __neg__(self):
#Return negated vector.
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -1 * self[j] 
        return result
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(x * other for x in self._coords))
        elif isinstance(other, Vector):
            return self.__dot__(other) 
        else:
            return NotImplemented
#Return scaled vector.
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * c        
        return result
    def __rmul__(self, scalar):
#Return right multiplied vector.
        return self.__mul__(scalar) 
    def __dot__(self, other):
#Return dot product  of two vectors.
        result = 0
        if len(self) != len(other): # relies on len method
            raise ValueError( "dimensions must agree" )
        for j in range(len(self)):
            result += self[j] * other[j] 
        return result
#Start with vector of zeros.
    def __eq__(self, other):
#Return True if vector has same coordinates as other.
        return self._coords == other._coords
    def __ne__(self, other):
#Return True if vector differs from other.
        return not self == other # rely on existing __eq__ definition
    def __str__(self):
#Produce string representation of vector.
        return  '<' + str(self._coords)[1:-1] + '>' 

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 * 2)        # Scalar multiplication: Vector(2, 4, 6)
print(2 * v1)        # Scalar multiplication from the left: Vector(2, 4, 6)
print(v1 * v2) 
