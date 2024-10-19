"""module for iterative fibonacci class"""

# System Imports

# First Party Imports
from abstract_fibonacci import AbstractFibonacci

# Third Party Imports


class IterativeFibonacci(AbstractFibonacci):
    """Iterative Fibonacci Solver class"""

    def _fibonacci_solver(self, n: int) -> int:
        """method to find value of nth number in sequence, iteratively"""
        value: int = None
        for item in range(n):

