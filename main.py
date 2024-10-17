#!/usr/bin/env python
"""bootstrap file"""

# System Imports
import sys

# First Party Imports
from program import run

# Third Party Imports


def main(*args):
    """main entry point for program"""
    # call run method
    run(*args)


# prevent running on import
if __name__ == "__main__":
    main(*sys.argv[1:])
else:
    raise ImportError("Run this file directly, dont import it.")
