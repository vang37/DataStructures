from typing import Iterable, Union

class Progression:
    def __init__(self, start: int = 0):
        self._current = start
    def _advance(self) -> None:
        self._current += 1
    def __next__(self) -> int:
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    def __iter__(self) -> Iterable[int]:
        return self
    def print_progression(self, n: int) -> None:
        print(' '.join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):
    def __init__(self, increment: int = 1, start: int = 0):
        super().__init__(start)
        self._increment = increment
    def _advance(self) -> None:
        self._current += self._increment

class GeometricProgression(Progression):
    def __init__(self, base: int = 2, start: int = 1):
        super().__init__(start)
        self._base = base
    def _advance(self) -> None:
        self._current *= self._base

class FibonacciProgression(Progression):
    def __init__(self, first: int = 0, second: int = 1):
        super().__init__(first)
        self._prev = second - first
    def _advance(self) -> None:
        self._prev, self._current = self._current, self._prev + self._current

class AbsDiffProgression(Progression):
    def __init__(self, first: int = 2, second: int = 200):
        super().__init__(first)
        self._prev = second + first
    def _advance(self) -> None:
        self._prev, self._current = self._current, abs(self._prev - self._current)

class SqRootProgression(Progression):
    def __init__(self, start: float = 65536):
        super().__init__(start)
        self._current = start
    def _advance(self) -> None:
        self._current = self._current**(1/2)

def main():
#    print('Default progression:')
#    Progression().print_progression(10)
#    print('Arithmetic progression with increment 5:')
#    ArithmeticProgression(5).print_progression(10)
#    print('Arithmetic progression with increment 5 and start 2:')
#    ArithmeticProgression(5, 2).print_progression(10)
#    print('Geometric progression with default base:')
#    GeometricProgression().print_progression(10)
#    print('Geometric progression with base 3:')
#    GeometricProgression(3).print_progression(10)
#    print('Fibonacci progression with default start values:')
#    FibonacciProgression().print_progression(10)
#    print('Fibonacci progression with start values 4 and 6:')
#    FibonacciProgression(4, 6).print_progression(10)
#    print('Fibonacci progression with start values 2 and 2:')
#    FibonacciProgression(2, 2).print_progression(8)
#    i, j, n = 1, 7, 60
#    for count in range(n):
#        print(count, "# of next_calls:", i, "exp_of_2: ", j)
#        i *= 2
#        j += 1
#        if j >= 63:
#            print("Solution: ", i + 1, "for exp: ", j)
#            break
#    print('Arithmetic Progression with increment 128:')
#    ArithmeticProgression(128).print_progression(10)
    print('AbsDiffProgression:')
    SqRootProgression().print_progression(18)
if __name__ == '__main__':
    main()
    
