class ReverseSequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = len(sequence)
    def __next__(self):
        self._k -= 1
        if self._k > -1: 
            return(self._seq[self._k])
        else:
            raise StopIteration( )
    def __iter__(self):
        return self

print([x for x in ReverseSequenceIterator([1,2,3,4,5,6,7,8])])
       
print([x for x in ReverseSequenceIterator([1,2,'d',4,56,7,8])])
