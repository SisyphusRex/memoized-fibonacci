"""memoized recursive module"""

# System Imports

# First Party Imports
from solver_modules.abstract_fibonacci import AbstractFibonacci

# Third Party Imports


class MemoizedRecursion(AbstractFibonacci):
    """class containing memoized recursion"""

    @property
    def name(self):
        return "Memoized Recursion"

    def _child_value_solver(self, n: int) -> int:
        if n in (0, 1):
            self.lookup_table[n] = n
            self.count += 1
            return n
        if n in self.lookup_table:
            # in python, checking for "x in y" when y is a dict is O(1)
            self.count += 1
            return self.lookup_table[n]

        value = self._child_value_solver(n - 2) + self._child_value_solver(n - 1)
        self.lookup_table[n] = value
        self.count += 1
        return value
