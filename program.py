"""run method for program"""

# System Imports
import sys

# First Party Imports
from recursive_fibonacci import RecursiveFibonacci
from iterative_fibonacci import IterativeFibonacci
from ui import UserInterface

# Third Party Imorts


def run():
    """method to run program"""

    ui = UserInterface()
    recursive_solver = RecursiveFibonacci()
    iterative_solver = IterativeFibonacci()

    running: bool = True
    while running:
        choice = ui.display_main_menu()
        match int(choice):
            # handles main menu functionality based on user input
            case 0:
                # talk about fibonacci sequence
                ui.explain_fibonacci()
                ui.press_any_key_to_continue()

            case 1:
                # run recursive fibonacci algorithm
                number_of_elements: int = int(ui.get_number_of_elements())
                recursive_solver.sequence_maker(number_of_elements)
                ui.print_sequence(recursive_solver)
                ui.press_any_key_to_continue()

            case 2:
                # run iterative fibonacci algorithm
                number_of_elements: int = int(ui.get_number_of_elements())
                iterative_solver.sequence_maker(number_of_elements)
                ui.print_sequence(iterative_solver)
                ui.press_any_key_to_continue()

            case 3:
                number_of_elements: int = int(ui.get_number_of_elements())
                recursive_solver.sequence_maker(number_of_elements)
                iterative_solver.sequence_maker(number_of_elements)
                ui.print_sequence(recursive_solver, iterative_solver)
                ui.press_any_key_to_continue()

            case 4:
                # exit
                sys.exit()
