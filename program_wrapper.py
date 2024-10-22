"""program wrapper module"""

# System Imports

# First Party Imports
from ui import UserInterface
from solver_modules.recursive_fibonacci import RecursiveFibonacci
from solver_modules.iterative_fibonacci import IterativeFibonacci
from solver_modules.memoized_recursion import MemoizedRecursion
from solver_modules.optimized_cache import OptimizedCache

# Third Party Imports


class ProgramWrapper:
    """ProgramWrapper class"""

    # This class will be used to encapsulate all of the
    # instantiations and method calls from the original program.
    # This will allow for the program file and run method to
    # only interact with the ProgramWrapper class, leading to
    # a clearer program run method

    def __init__(self):
        """constructor"""
        self.__ui = UserInterface()
        self.__recursive_solver = RecursiveFibonacci()
        self.__iterative_solver = IterativeFibonacci()
        self.__memoized_solver = MemoizedRecursion()
        self.__optimized_cache_solver = OptimizedCache()

    #################
    # Intro Methods #
    #################
    def get_main_menu_choice(self) -> str:
        """menu method to display main menu and get choice"""
        return self.__ui.display_main_menu()

    ##########################
    # Main Menu Methods      #
    ##########################
    def explain_fibonacci(self) -> None:
        """menu method to explain fibonacci"""
        self.__ui.explain_fibonacci()
        self.__ui.press_enter_to_continue()

    def get_sequence_menu_choice(self) -> str:
        """menu method to display sequence menu and get choice"""
        return self.__ui.display_sequence_menu()

    def get_value_finder_menu_choice(self) -> str:
        """menu method to display value solver menu and get choice"""
        return self.__ui.display_value_finder_menu()

    #########################
    # Sequence Menu Methods #
    #########################
    def create_recursive_sequence(self) -> None:
        """menu method to create sequence with recursion"""
        number_of_elements: int = int(self.__ui.get_number_of_elements())
        self.__recursive_solver.sequence_maker(number_of_elements)
        self.__ui.print_sequence(self.__recursive_solver)
        self.__ui.press_enter_to_continue()

    def create_iterative_sequence(self) -> None:
        """menu method to create sequence with iteration"""
        number_of_elements: int = int(self.__ui.get_number_of_elements())
        self.__iterative_solver.sequence_maker(number_of_elements)
        self.__ui.print_sequence(self.__iterative_solver)
        self.__ui.press_enter_to_continue()

    def create_memoized_sequence(self) -> None:
        """menu method to create sequence with memoization"""
        number_of_elements: int = int(self.__ui.get_number_of_elements())
        self.__memoized_solver.sequence_maker(number_of_elements)
        self.__ui.print_sequence(self.__memoized_solver)
        self.__ui.press_enter_to_continue()

    def create_optimized_cache_sequence(self) -> None:
        """menu method to create sequence with optimized cache"""
        number_of_elements: int = int(self.__ui.get_number_of_elements())
        self.__optimized_cache_solver.sequence_maker(number_of_elements)
        self.__ui.print_sequence(self.__optimized_cache_solver)
        self.__ui.press_enter_to_continue()

    def clear_cache(self) -> None:
        """menu method to clear cache of memoized and optimized"""
        self.__memoized_solver.lookup_table.clear()
        self.__optimized_cache_solver.lookup_table.clear()
        self.__ui.print_cleared()

    def compare_sequences_by_algorithm(self) -> None:
        """menu method to compare sequences"""
        number_of_elements: int = int(self.__ui.get_number_of_elements())
        self.__recursive_solver.sequence_maker(number_of_elements)
        self.__iterative_solver.sequence_maker(number_of_elements)
        self.__memoized_solver.sequence_maker(number_of_elements)
        self.__optimized_cache_solver.sequence_maker(number_of_elements)
        self.__ui.print_sequence(
            self.__iterative_solver,
            self.__recursive_solver,
            self.__memoized_solver,
            self.__optimized_cache_solver,
        )
        self.__ui.press_enter_to_continue()

    def compare_sequence_n_cycle_dicts(self) -> None:
        """menu method to compare n to cycle dicts"""
        self.__ui.print_dict(
            self.__iterative_solver.name, self.__iterative_solver.sequence_n_cycle_dict
        )
        self.__ui.print_dict(
            self.__recursive_solver.name, self.__recursive_solver.sequence_n_cycle_dict
        )

        self.__ui.print_dict(
            self.__memoized_solver.name, self.__memoized_solver.sequence_n_cycle_dict
        )
        self.__ui.print_dict(
            self.__optimized_cache_solver.name,
            self.__optimized_cache_solver.sequence_n_cycle_dict,
        )
        self.__ui.press_enter_to_continue()

    #############################
    # Value Finder Menu Methods #
    #############################
    def find_value_with_iteration(self) -> None:
        """menu method to find value at index with iteration"""
        index: int = int(self.__ui.get_index_of_sequence()) - 1
        self.__iterative_solver.value_finder(index)
        self.__ui.print_value(self.__iterative_solver)
        self.__ui.press_enter_to_continue()

    def find_value_with_recursion(self) -> None:
        """menu method to find value at index with recursion"""
        index: int = int(self.__ui.get_index_of_sequence()) - 1
        self.__recursive_solver.value_finder(index)
        self.__ui.print_value(self.__recursive_solver)
        self.__ui.press_enter_to_continue()

    def find_value_with_memoized_recursion(self) -> None:
        """menu method to find value at index with memoized recursion"""
        index: int = int(self.__ui.get_index_of_sequence()) - 1
        self.__memoized_solver.value_finder(index)
        self.__ui.print_value(self.__memoized_solver)
        self.__ui.press_enter_to_continue()

    def find_value_with_optimized_cache(self) -> None:
        """menu method to find value at index with optimized cache"""
        index: int = int(self.__ui.get_index_of_sequence()) - 1
        self.__optimized_cache_solver.value_finder(index)
        self.__ui.print_value(self.__optimized_cache_solver)
        self.__ui.press_enter_to_continue()

    def compare_value_n_cycle_dicts(self) -> None:
        """menu method to compare value n/cyle dicts"""
        self.__ui.print_dict(
            self.__iterative_solver.name, self.__iterative_solver.value_n_cycle_dict
        )
        self.__ui.print_dict(
            self.__recursive_solver.name, self.__recursive_solver.value_n_cycle_dict
        )

        self.__ui.print_dict(
            self.__memoized_solver.name, self.__memoized_solver.value_n_cycle_dict
        )
        self.__ui.print_dict(
            self.__optimized_cache_solver.name,
            self.__optimized_cache_solver.value_n_cycle_dict,
        )
        self.__ui.press_enter_to_continue()

    def compare_value_by_algorithm(self) -> None:
        """method to compare algorithms in finding one value"""
        index: int = int(self.__ui.get_index_of_sequence()) - 1
        self.__recursive_solver.value_finder(index)
        self.__iterative_solver.value_finder(index)
        self.__memoized_solver.value_finder(index)
        self.__optimized_cache_solver.value_finder(index)
        self.__ui.print_value(
            self.__iterative_solver,
            self.__recursive_solver,
            self.__memoized_solver,
            self.__optimized_cache_solver,
        )
        self.__ui.press_enter_to_continue()
