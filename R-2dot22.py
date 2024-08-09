from abc import ABCMeta, abstractmethod 
from typing import Iterable, Iterator

class Sequence(metaclass=ABCMeta):

    @abstractmethod 
    def __iter__(self) -> Iterator:
        pass
    
    @abstractmethod 
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __getitem__(self, j):
        pass

    def __contains__(self, val) -> bool:
        for j in range(len(self)):
            if self[j] == val: 
                return True
        return False

    def index(self, val) -> int:
        for j in range(len(self)):
            if self[j] == val: 
                return j
        raise ValueError('value not in sequence')
    
    def count(self, val) -> int:
        k = 0
        for j in range(len(self)):
            if self[j] == val: 
                k += 1
        return k

    def __eq__(self, other) -> bool:
        if len(self) != len(other):
            return False 
        for j in range(len(self)):
            if self[j] != other[j]:
                return False
        return True

    def __lt__(self, other) -> bool:
        if len(self) == 0 or len(other) == 0:
            return "This test won't work in this case."
        for s, o in zip(self, other):
            if str(s).lower() < str(o).lower():
                return True
            elif str(s).lower() > str(o).lower():
                return False
        return  len(self) < len(other)

# Example implementation of a concrete sequence class
class ListSequence(Sequence):
    def __init__(self, data):
        self._data = list(data)

    def __iter__(self) -> Iterator:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, j):
        if j < 0 or j >= len(self._data):
            raise IndexError("Index out of bounds")
        return self._data[j]

seq1 = ListSequence([1, 2, 3, 4])
seq2 = ListSequence([1, 2, 3, 5])
seq3 = ListSequence([1, 2, 3])

print(seq1 < seq2) 
print(seq1 < seq3) 
print(seq3 < seq1) 
