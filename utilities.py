"""utilities module"""

# System imports

# First Party Imports
from abstract_fibonacci import AbstractFibonacci

# Third Party Imports


class Utilities:
    """utility function class"""

    ############
    # Methods  #
    ############
    def create_n_cycle_dict(
        self, n: int, solver_object: AbstractFibonacci
    ) -> dict[int, int]:
        """method to create n cycle dict"""
        cycle_dict: dict[int, int] = {}
        for number in range(1, n + 1):
            solver_object.sequence_maker(number)
            cycle_dict[number] = solver_object.count
        return cycle_dict
