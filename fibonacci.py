"""file for fibonacci class"""

# System Imports

# First Party Imports

# Third Party Imports


class Fibonacci:
    """Fibonacci class"""

    def solver(self, n: int) -> list:
        """method to solve fibonacci sequence for n items"""
        if n in (0, 1):
            return n
        return self.solver(n - 2) + self.solver(n - 1)
