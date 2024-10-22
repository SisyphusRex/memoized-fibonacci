"""user interface module"""

# System Imports

# First Party Imports
from colors import print_blue, print_green, print_red, print_magenta, print_yellow

# Third Party Imports


class UserInterface:
    """User Interface class"""

    MAIN_MENU: list[str] = [
        "Explain Fibonacci",
        "Create Sequences",
        "Find Values",
        "Exit",
    ]

    SEQUENCE_MENU: list[str] = [
        "Create Sequence with Iteration",
        "Create Sequence with Recursion",
        "Create Sequence with Memoized Recursion",
        "Create Sequence with Optimized Cache Memoized Recursion",
        "Compare Sequence using Each Algorithm",
        "Clear Cache",
        "Show n/cycle Charts\n      (n= number of elements in sequence)",
        "Exit to Main Menu",
    ]

    VALUE_FINDER_MENU: list[str] = [
        "Find Index Value using Iteration",
        "Find Index Value using Recursion",
        "Find Index Value using Memoized Recursion",
        "Find Index Value using Optomized Cache Memoized Recursion",
        "Find Value using Each Algorithm",
        "Clear Cache",
        "Show n/cycle Charts\n        (n= nth number in sequence)",
        "Exit to Main Menu",
    ]

    #########################
    # Public Methods         #
    #########################

    def display_value_finder_menu(self) -> str:
        """method to display value solver menu and return choice"""
        user_input: str = self.__while_waiting_for_good_menu_input(
            self.VALUE_FINDER_MENU
        )
        return user_input

    def display_sequence_menu(self) -> str:
        """method to display sequence menu and return choice"""
        user_input: str = self.__while_waiting_for_good_menu_input(self.SEQUENCE_MENU)
        return user_input

    def display_main_menu(self) -> str:
        """method to display menu, get input, and return selection"""
        user_input: str = self.__while_waiting_for_good_menu_input(self.MAIN_MENU)
        return user_input

    def explain_fibonacci(self) -> None:
        """method to print out explanation"""
        print_blue(
            "The Fibonacci sequence is a sequence in mathematics in which each number is the sum of the two preceding numbers.\n\n"
            "F₀ = 0, F₁ = 1\n"
            "Fₙ = Fₙ₋₁ + Fₙ₋₂\n\n"
            "Which produces:\n"
            "0 1 1 2 3 5 8 13 ...\n\n"
            "For this program, we will always start the sequence at 0."
        )
        print()

    def get_index_of_sequence(self) -> str:
        """method to get index of fibonacci sequence"""
        user_input: str = self.__while_waiting_for_good_index_input()
        # we must subtract 1 to make the user input an index and then recast it to string for uniformity
        user_input = int(user_input) - 1
        return str(user_input)

    def get_number_of_elements(self) -> str:
        """method to get number of elements for fibonacci sequence"""
        user_input: str = self.__while_waiting_for_good_elements_input()
        return user_input

    def press_enter_to_continue(self) -> None:
        """pauses printing to terminal until key pressed"""
        print_green("Press Enter to continue.")
        user_input = input()
        print()
        if user_input:
            pass

    def print_sequence(self, *args) -> None:
        """method to print fibonacci sequence and stats"""
        print_magenta(args[0].sequence)
        header: list[str] = ["Name", "Cycles", "Runtime"]
        # TODO: I cannot figure out why the header does not match up with the string in the abstract __str__ call
        print_blue(f"{header[0]:<20}{header[1]:>15}{header[2]:>15}")
        # f"{self._name:<15}{self.__format_count(self.count):>20}{self.__format_time(self.timer):>15}"
        for index, value in enumerate(args):
            print(value)
        print()

    def print_value(self, *args) -> None:
        """method to print value at index and stats"""
        print_magenta(args[0].value)
        header: list[str] = ["Name", "Cycles", "Runtime"]
        # TODO: I cannot figure out why the header does not match up with the string in the abstract __str__ call
        print_blue(f"{header[0]:<20}{header[1]:>15}{header[2]:>15}")
        # f"{self._name:<15}{self.__format_count(self.count):>20}{self.__format_time(self.timer):>15}"
        for index, value in enumerate(args):
            print(value)
        print()

    def print_dict(self, algorithm_name: str, input_dict: dict) -> None:
        """method to print dict"""
        header: list[str] = ["n", "Cycles"]
        print_magenta(algorithm_name)
        print_blue(f"{header[0]:>10}{header[1]:>10}")
        for key, value in input_dict.items():
            print(f"{key:>10}{value:>10}")

    def print_cleared(self) -> None:
        """print cache cleared"""
        print_yellow("Cache cleared.")
        print()

    ####################
    # Private Methods   #
    ####################
    def __display_menu_base(self, menu: list[str]) -> None:
        """method to display main menu, get input, and return selection inside validation loop"""
        print_green("Type the number of your selection:")
        for index, text in enumerate(menu):
            print(f"{index:<3}{text}")

    def __get_number_of_elements_base(self) -> None:
        """method to display get elements message"""
        print_green("How many Fibonacci elements do you want to display?")

    def __get_index_of_sequence_base(self) -> None:
        """method to display get index message"""
        print_green(
            "Which number of the Fibonacci sequence do you want the value of?\n(number = nth number in sequence\n1 for first, 2 for second, etc.)"
        )

    def __while_waiting_for_good_index_input(self) -> str:
        """method to repeat message and input until good"""
        good_input: bool = False
        while not good_input:
            self.__get_index_of_sequence_base()
            user_input = input(">")
            print()
            good_input = self.__is_positive_integer(user_input)
        return user_input

    def __while_waiting_for_good_elements_input(self) -> str:
        """method to repeat message and input until good"""
        good_input: bool = False
        while not good_input:
            self.__get_number_of_elements_base()
            user_input = input(">")
            print()
            good_input = self.__is_positive_integer(user_input)
        return user_input

    def __while_waiting_for_good_menu_input(self, menu: list[str]) -> str:
        """method to repeat menu and input until good"""
        good_input: bool = False
        while not good_input:
            self.__display_menu_base(menu)
            user_input = input(">")
            print()
            good_input = self.__validate_user_input(user_input, menu)
        return user_input

    def __validate_user_input(self, user_input: str, menu: list[str]) -> bool:
        """method to validate input if tests pass"""
        if not self.__is_integer(user_input):
            return False
        if not self.__is_in_menu(user_input, menu):
            return False
        return True

    def __is_integer(self, user_input: str) -> bool:
        """method to check if integer"""
        try:
            int(user_input)
        except ValueError:
            print_red("Must type an integer.")
            print()
            return False
        return True

    def __is_in_menu(self, user_input: str, menu: list[str]) -> bool:
        """method to check if in menu"""
        if int(user_input) not in range(len(menu)):
            print_red("Not in Menu range.")
            print()
            return False
        return True

    def __is_positive_integer(self, user_input: str) -> bool:
        """method to check if positive integer"""
        if not self.__is_integer(user_input):
            return False
        if int(user_input) <= 0:
            print_red("Must be positive")
            print()
            return False
        return True
