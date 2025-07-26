# Copyright 2025 Theodore Podewil
# GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 



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
