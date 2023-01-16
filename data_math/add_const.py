#!/usr/bin/env python3
# ADD CONST.py
#   by Lut99
#
# Created:
#   16 Jan 2023, 13:41:26
# Last edited:
#   16 Jan 2023, 13:50:18
# Auto updated?
#   Yes
#
# Description:
#   Implements an element-wise addition of a dataset and some constant.
#

import argparse
import os
import sys


##### GENERATION FUNCTIONS #####
def add_vector(data: str, const: float) -> int:
    """
        Generates a zeroes file with the vector layout.

        Specifically, generates a file /result/data with `n` (ASCII) constants,
        delimited by spaces.  Their value is the element-wise addition of the
        input `data` and the given `const`.

        # Arguments
        - `data`: The path to the dataset folder that we are operating on. We assume there is a `data` file within it.
        - `const`: The constant to add to each element.

        # Returns
        The return code of the operation. `0` means success.
    """

    # Read the input
    try:
        with open(os.path.join(data, "data"), "r") as source:
            vec = source.read()
    except IOError as e:
        print(f"Failed to read from input file '{os.path.join(data, 'data')}': {e}", file=sys.stderr)
        return e.errno

    # Split it and attempt to parse as real values
    vec = [ float(v) for v in vec.split() ]

    # Add the constant
    vec = [ v + const for v in vec ]

    # Write back, trying to write as integers whenever possible
    try:
        # Attempt to open the output file
        with open("/result/data", "w") as target:
            for i in range(len(vec)):
                if i > 0: target.write(" ")
                if float(int(vec[i])) == vec[i]:
                    target.write(f"{int(vec[i])}")
                else:
                    target.write(f"{vec[i]}")
    except IOError as e:
        print(f"Failed to write to output file '/result/data': {e}", file=sys.stderr)
        return e.errno

    # Done
    return 0





##### ENTRYPOINT #####
def main(data: str, const: float, kind: str) -> int:
    """
        Entrypoint to the script.

        # Arguments
        - `data`: The path to the dataset folder that we are operating on.
        - `const`: The constant to add to each element.
        - `kind`: The kind of dataset to generate.

        # Returns
        The exit code for the script. `0` means success.
    """

    # Match on the kind
    if kind == "vector":
        return add_vector(data, const)

    # Should never happen
    raise RuntimeError(f"main() saw a non-allowed kind '{kind}' (should have been taken care of by the argument parser)")



# The actual entrypoint
if __name__ == "__main__":
    # Parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("DATA", type=str, help="The path to the input data directory.")
    parser.add_argument("CONST", type=float, help="The constant to add to each element.")
    parser.add_argument("KIND", choices=["vector"], help="The kind of dataset to generate.")
    args = parser.parse_args()

    # Call main
    exit(main(args.DATA, args.CONST, args.KIND))
