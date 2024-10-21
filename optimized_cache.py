"""optimized cache memoized recursion module"""

# System Imports

# First Party Imports
from abstract_fibonacci import AbstractFibonacci

# Third Party Imports


class OptimizedCache(AbstractFibonacci):
    """Optimized Cache Memoized Recursion class"""

    @property
    def name(self):
        return "Optimized Cache"

    def _fibonacci_value_solver(self, n: int) -> int:
        if n in (0, 1):
            self.lookup_table[n] = n
            self.count += 1
            return n
        if n in self.lookup_table:
            self.count += len(self.lookup_table)
            return self.lookup_table[n]

        value = self._fibonacci_value_solver(n - 2) + self._fibonacci_value_solver(
            n - 1
        )
        self.lookup_table[n] = value
        # this optimizes our cache by getting rid of the key, value pair that is no longer needed each time we add a
        # new key value
        del self.lookup_table[n - 2]
        self.count += 1
        return value
