"""file for fibonacci class"""

# System Imports

# First Party Imports
from solver_modules.abstract_fibonacci import AbstractFibonacci

# Third Party Imports


class RecursiveFibonacci(AbstractFibonacci):
    """Recursive Fibonacci sequence class"""

    @property
    def name(self):
        return "Recursive"

    def _fibonacci_value_solver(self, n: int) -> int:
        self.count += 1
        if n in (0, 1):
            return n
        return self._fibonacci_value_solver(n - 2) + self._fibonacci_value_solver(n - 1)
