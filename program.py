"""run method for program"""

# System Imports
import sys

# First Party Imports
from recursive_fibonacci import RecursiveFibonacci
from ui import UserInterface

# Third Party Imorts


def run():
    """method to run program"""

    ui = UserInterface()
    recursive_solver = RecursiveFibonacci()

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
                # run original fibonacci algorithm
                number_of_elements = ui.get_number_of_elements()
                print(recursive_solver.solver(int(number_of_elements)))

            case 2:
                # run modified fibonacci algorithm
                ...

            case 3:
                # exit
                sys.exit()
