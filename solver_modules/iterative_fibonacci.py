# Copyright 2025 Theodore Podewil
# GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 



"""module for iterative fibonacci class"""

# System Imports

# First Party Imports
from solver_modules.abstract_fibonacci import AbstractFibonacci

# Third Party Imports


class IterativeFibonacci(AbstractFibonacci):
    """Iterative Fibonacci Solver class"""

    @property
    def name(self):
        return "Iteration"

    def _child_value_solver(self, n: int) -> int:
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
