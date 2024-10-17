"""run method for program"""

# System Imports
import sys

# First Party Imports
from fibonacci import Fibonacci

# Third Party Imorts


def run():
    """method to run program"""

    my_fibonacci = Fibonacci()

    print("Give me the number of items in fibonacci sequence to solve for: ")
    user_input = input(">")

    my_list = [my_fibonacci.solver(item) for item in range(int(user_input))]

    print(my_list)

    sys.exit(0)
