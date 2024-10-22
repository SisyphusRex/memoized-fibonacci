"""abstract fibonacci class module"""

# System Imports
from abc import ABC, abstractmethod
from time import perf_counter

# First Party Imports

# Third Party Imports


class AbstractFibonacci(ABC):
    """fibonacci abstract class"""

    ###############
    # Constructors#
    ###############
    def __init__(self):
        """constructor"""
        self.sequence: list = []
        self.timer: float = 0.00
        self.count: int = 0
        self.lookup_table: dict = {}  # AKA cache
        self.value: int = 0

    ################
    # Interfaces    #
    ################
    @property
    @abstractmethod
    def name(self):
        """name of fibonacci class property"""

    @abstractmethod
    def _child_value_solver(self, n: int) -> int:
        """method to do the math to find fibonacci value of nth number in sequence"""

    ###############
    # Properties  #
    ###############
    @property
    def value_n_cycle_dict(self) -> dict[int, int]:
        """method to get valu n/cycle dict"""
        cycle_dict: dict[int, int] = {}
        for number in range(1, 11):
            self.value_finder(number)
            cycle_dict[number] = self.count
            self.count = 0
        return cycle_dict

    @property
    def sequence_n_cycle_dict(self) -> dict[int, int]:
        """method to get sequence n cycle dict"""
        cycle_dict: dict[int, int] = {}
        for number in range(1, 11):
            self.sequence_maker(number)
            cycle_dict[number] = self.count
            self.lookup_table.clear()
        return cycle_dict

    #################
    # Public Methods#
    #################
    def __str__(self):
        """str method"""
        # TODO: I cannot figure out why this string does not match up with the header in the ui.a
        return f"{self.name:<20}{self.__format_count(self.count):>15}{self.__format_time(self.timer):>15}"

    def sequence_maker(self, number_of_elements: int):
        """method to create fibonacci sequence"""
        # this creates a fibonacci sequence in the form of a list of each nth value (provided by the solver)
        self.count = 0
        self.timer = 0.00
        self.sequence = []
        timer_start: float = perf_counter()
        self.sequence = [
            self._child_value_solver(index) for index in range(number_of_elements)
        ]
        timer_stop: float = perf_counter()
        self.timer = timer_stop - timer_start

    def value_finder(self, index: int) -> int:
        """method to find value of sequence index"""
        self.count = 0
        self.timer = 0.00
        self.value = 0
        timer_start: float = perf_counter()
        self.value: int = self._child_value_solver(index)
        timer_stop: float = perf_counter()
        self.timer = timer_stop - timer_start

    ##################
    # Private Methods#
    ##################
    def __format_time(self, time: float) -> str:
        return f"{time:.7f}"

    def __format_count(self, count: int) -> str:
        return f"{count:,}"
