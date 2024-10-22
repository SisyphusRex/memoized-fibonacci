"""memoized recursive module"""

# System Imports

# First Party Imports
from solver_modules.abstract_fibonacci import AbstractFibonacci

# Third Party Imports


class MemoizedRecursion(AbstractFibonacci):
    """class containing memoized recursion"""

    @property
    def name(self):
        return "MemoizedRecursion"

    def _child_value_solver(self, n: int) -> int:
        if n in (0, 1):
            self.lookup_table[n] = n
            self.count += 1
            return n
        if n in self.lookup_table:
            # we must increase our count by the length of the look up table, since
            # the number of process to compare n to lookup_table grows in direct
            # relation to n
            self.count += len(self.lookup_table)
            return self.lookup_table[n]

        value = self._child_value_solver(n - 2) + self._child_value_solver(n - 1)
        self.lookup_table[n] = value
        self.count += 1
        return value
