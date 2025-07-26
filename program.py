# Copyright 2025 Theodore Podewil
# GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 



"""run method for program"""

# System Imports
import sys

# First Party Imports
from program_wrapper import ProgramWrapper


# Third Party Imorts


def run():
    """method to run program"""
    program = ProgramWrapper()

    while True:
        main_menu_choice: str = program.get_main_menu_choice()
        match int(main_menu_choice):
            # handles main menu functionality based on user input
            case 0:
                # talk about fibonacci sequence
                program.explain_fibonacci()

            case 1:
                # Sequence Maker menu
                while True:
                    sequence_menu_choice: str = program.get_sequence_menu_choice()
                    match int(sequence_menu_choice):
                        case 0:
                            # create sequence with iteration
                            program.create_iterative_sequence()
                        case 1:
                            # create sequence with recursion
                            program.create_recursive_sequence()
                        case 2:
                            # create sequence with memoized recursion
                            program.create_memoized_sequence()
                        case 3:
                            # create sequence with optimized cache
                            program.create_optimized_cache_sequence()
                        case 4:
                            # compare sequences by algorithm
                            program.compare_sequences_by_algorithm()
                        case 5:
                            # clear memoized caches
                            program.clear_cache()
                        case 6:
                            # compare n/cycle dicts
                            program.compare_sequence_n_cycle_dicts()
                        case 7:
                            # exit to main menu
                            break
            case 2:
                # Value solver menu
                while True:
                    value_finder_menu_choice: str = (
                        program.get_value_finder_menu_choice()
                    )
                    match int(value_finder_menu_choice):
                        case 0:
                            # find value using iteration
                            program.find_value_with_iteration()
                        case 1:
                            # find value using recursion
                            program.find_value_with_recursion()
                        case 2:
                            # find value using memoized recursion
                            program.find_value_with_memoized_recursion()
                        case 3:
                            # find value using optimized cache
                            program.find_value_with_optimized_cache()
                        case 4:
                            # compare values by algorithm
                            program.compare_value_by_algorithm()
                        case 5:
                            # clear memoized caches
                            program.clear_cache()
                        case 6:
                            # compare n/cycle dicts
                            program.compare_value_n_cycle_dicts()
                        case 7:
                            # exit to main menu
                            break
            case 3:
                # exit
                sys.exit()
