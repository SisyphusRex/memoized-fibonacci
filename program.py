"""run method for program"""

# System Imports
import sys

# First Party Imports
from solver_modules.recursive_fibonacci import RecursiveFibonacci
from solver_modules.iterative_fibonacci import IterativeFibonacci
from ui import UserInterface
from solver_modules.memoized_recursion import MemoizedRecursion
from solver_modules.optimized_cache import OptimizedCache

# Third Party Imorts


def run():
    """method to run program"""

    ui = UserInterface()
    recursive_solver = RecursiveFibonacci()
    iterative_solver = IterativeFibonacci()
    memoized_solver = MemoizedRecursion()
    optimized_cache_solver = OptimizedCache()

    running: bool = True
    while running:
        choice = ui.display_main_menu()
        match int(choice):
            # handles main menu functionality based on user input
            case 0:
                # talk about fibonacci sequence
                ui.explain_fibonacci()
                ui.press_enter_to_continue()

            case 1:
                # run recursive fibonacci algorithm
                number_of_elements: int = int(ui.get_number_of_elements())
                recursive_solver.sequence_maker(number_of_elements)
                ui.print_sequence(recursive_solver)
                ui.press_enter_to_continue()

            case 2:
                # run iterative fibonacci algorithm
                number_of_elements: int = int(ui.get_number_of_elements())
                iterative_solver.sequence_maker(number_of_elements)
                ui.print_sequence(iterative_solver)
                ui.press_enter_to_continue()

            case 3:
                # run memoized recursive algorithm
                number_of_elements: int = int(ui.get_number_of_elements())
                memoized_solver.sequence_maker(number_of_elements)
                ui.print_sequence(memoized_solver)

            case 4:
                # run optimized cache memoized recursive algorithm
                number_of_elements: int = int(ui.get_number_of_elements())
                optimized_cache_solver.sequence_maker(number_of_elements)
                ui.print_sequence(optimized_cache_solver)

            case 5:
                # clear memoization cache
                memoized_solver.lookup_table.clear()
                optimized_cache_solver.lookup_table.clear()
                ui.print_cleared()

            case 6:
                # compare algorithms
                number_of_elements: int = int(ui.get_number_of_elements())
                recursive_solver.sequence_maker(number_of_elements)
                iterative_solver.sequence_maker(number_of_elements)
                memoized_solver.sequence_maker(number_of_elements)
                optimized_cache_solver.sequence_maker(number_of_elements)
                ui.print_sequence(
                    recursive_solver,
                    iterative_solver,
                    memoized_solver,
                    optimized_cache_solver,
                )
                ui.press_enter_to_continue()

            case 7:
                # compare cycle dicts
                ui.print_dict(recursive_solver.name, recursive_solver.n_cycle_dict)
                ui.print_dict(iterative_solver.name, iterative_solver.n_cycle_dict)
                ui.print_dict(memoized_solver.name, memoized_solver.n_cycle_dict)
                ui.print_dict(
                    optimized_cache_solver.name, optimized_cache_solver.n_cycle_dict
                )

            case 8:
                # exit
                sys.exit()
