"""abstract fibonacci class module"""

# System Imports
from abc import ABC, abstractmethod
from time import perf_counter

# First Party Imports

# Third Party Imports


class AbstractFibonacci(ABC):
    """fibonacci abstract class"""

    def __init__(self):
        self.sequence: list = []
        self.timer: float = 0.00
        self.count: int = 0

    def __str__(self):
        """str method"""
        # TODO: I cannot figure out why this string does not match up with the header in the ui.
        return f"{self._name:<15}{self.__format_count(self.count):>20}{self.__format_time(self.timer):>15}"

    def sequence_maker(self, number_of_elements: int) -> list[int]:
        """method to create fibonacci sequence"""
        # this creates a fibonacci sequence in the form of a list of each nth value (provided by the solver)
        self.count = 0
        self.timer = 0.00
        self.sequence = []
        timer_start: float = perf_counter()
        self.sequence = [
            self._fibonacci_value_solver(n) for n in range(number_of_elements)
        ]
        timer_stop: float = perf_counter()
        self.timer = timer_stop - timer_start

    @abstractmethod
    def _fibonacci_value_solver(self, n: int) -> int:
        """method to do the math to find fibonacci value of nth number in sequence"""

    @property
    @abstractmethod
    def _name(self):
        """name of fibonacci class property"""

    #################
    # Private        #
    #################
    def __format_time(self, time: float) -> str:
        return f"{time:.7f}"

    def __format_count(self, count: int) -> str:
        return f"{count:,}"
