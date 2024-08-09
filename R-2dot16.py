
#The formula max(0, (stop - start + step - 1) // step) efficiently computes the 
# number of elements in a range by adjusting the span and ensuring non-negative results. 
#It accounts for the arithmetic sequence and correctly handles various cases including 
# empty ranges and non-aligned end values.

##Justification of the Formula
#Correct Calculation of Number of Steps:
#
#Consider the start value start and the end value stop with step size step.
#To find how many steps fit between start and stop, you need to compute how 
#many increments of step can fit in the interval [start, stop).
#
#Adding step - 1 to stop - start effectively handles cases where the end value might 
#not align perfectly with a step increment.
#
#For example:
#If start = 0, stop = 10, and step = 3, the sequence is 0, 3, 6, 9. Here, the total 
#length is 4 steps.
#
#Without the adjustment + step - 1, the integer division would be (10 - 0) // 3 = 3, 
#which misses the last element (9).
#
##Handling Negative and Zero Values:
#If stop <= start, the range should be empty. Adding step - 1 and then taking max(0, ...) 
#ensures that negative results are clamped to zero, indicating no elements in the range.
#
#For example:
#If start = 5, stop = 5, and step = 3, the range is empty. 
#Here, max(0, (5 - 5 + 3 - 1) // 3) = max(0, 0) = 0.
#
##Ensuring Positive Step Size:
#The formula assumes a positive step. For negative step, the calculations would need adjustments, 
#but in this context, it assumes the range only has positive increments.

class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start
        
        self._start = start
        self._stop = stop
        self._step = step
        
        self._length = max(0, (stop - start + step - 1) // step)
    
    def __len__(self):
        return self._length
    
    def __getitem__(self, k):
        if k < 0:
            k += len(self)
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        return self._start + k * self._step
    
    def __contains__(self, value):
        if (value - self._start) % self._step == 0 and self._start <= value < self._stop:
            return True
        return False

# Example usage
r = Range(10, 50, 5)
print(15 in r)  # True
print(17 in r)  # False
print(50 in r)  # False (since the stop is exclusive)

