"""module for iterative fibonacci class"""

# System Imports

# First Party Imports
from abstract_fibonacci import AbstractFibonacci

# Third Party Imports


class IterativeFibonacci(AbstractFibonacci):
    """Iterative Fibonacci Solver class"""

    @property
    def name(self):
        return "Iterative"

    def _fibonacci_value_solver(self, n: int) -> int:
        if n == 0:
            self.count += 1
            return 0
        if n == 1:
            self.count += 1
            return 1

        my_list: list = []
        # here we must use the range of n + 1 because n is the index of the sequence
        for item in range(n + 1):
            if item == 0:
                my_list.append(0)
                self.count += 1
            elif item == 1:
                my_list.append(1)
                self.count += 1
            else:
                my_list.append(my_list[item - 2] + my_list[item - 1])
                self.count += 1

        return my_list[n]
