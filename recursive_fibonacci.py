"""file for fibonacci class"""

# System Imports

# First Party Imports
from abstract_fibonacci import AbstractFibonacci

# Third Party Imports


class RecursiveFibonacci(AbstractFibonacci):
    """Recursive Fibonacci sequence class"""

    def _fibonacci_solver(self, n: int) -> int:
        """method to solve value of nth number in sequence, recursively"""
        if n in (0, 1):
            return n
        return self._fibonacci_solver(n - 2) + self._fibonacci_solver(n - 1)
