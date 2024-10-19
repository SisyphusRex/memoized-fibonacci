"""abstract fibonacci class module"""

# System Imports
from abc import ABC, abstractmethod

# First Party Imports

# Third Party Imports


class AbstractFibonacci(ABC):
    """fibonacci abstract class"""

    def solver(self, number_of_elements: int) -> list[int]:
        """method to create fibonacci sequence"""
        # this creates a fibonacci sequence by creating a list of each value of each
        # index in the range of given number of elements
        sequence: list[int] = [
            self._fibonacci_solver(index) for index in range(number_of_elements)
        ]
        return sequence

    @abstractmethod
    def _fibonacci_solver(self, n: int) -> int:
        """method to do the math to find fibonacci value of nth number in sequence"""
