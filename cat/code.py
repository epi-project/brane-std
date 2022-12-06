#!/usr/bin/env python3
# CODE.py
#   by Lut99
#
# Created:
#   06 Dec 2022, 15:14:47
# Last edited:
#   06 Dec 2022, 15:41:34
# Auto updated?
#   Yes
#
# Description:
#   Implements the code for the `cat` package (see the README.md file).
#

import base64
import json
import os
import sys


##### FUNCTION FUNCTIONS #####
def cat(dataset: str, path: str) -> str:
    """
        Implements the `func cat(dataset, path)` function.
    """

    # Compute the total path
    path = os.path.join(dataset, path) if path != "-" else dataset

    # Attempt to open the file
    try:
        with open(path, "r") as h:
            return h.read()
    except IOError as e:
        print(f"Failed to read file '{path}': {e}", file=sys.stderr)
        exit(1)

def cat_base64(dataset: str, path: str) -> str:
    """
        Implements the `func cat_base64(dataset, path)` function.
    """

    # Compute the total path
    path = os.path.join(dataset, path) if path != "-" else dataset

    # Attempt to open the file
    try:
        with open(path, "rb") as h:
            # Return it encoded
            return base64.b64encode(h.read()).decode("UTF-8")
    except IOError as e:
        print(f"Failed to read file '{path}': {e}", file=sys.stderr)
        exit(1)

def cat_range(dataset: str, path: str, start: int, end: int) -> str:
    """
        Implements the `func cat_range(dataset, path, start, end)` function.
    """

    # Compute the total path
    path = os.path.join(dataset, path) if path != "-" else dataset

    # Attempt to open the file
    try:
        with open(path, "r") as h:
            # Seek the correct position first
            h.seek(start)
            return h.read(1 + end - start)
    except IOError as e:
        print(f"Failed to read file '{path}': {e}", file=sys.stderr)
        exit(1)

def cat_range_base64(dataset: str, path: str, start: int, end: int) -> str:
    """
        Implements the `func cat_range_base64(dataset, path, start, end)` function.
    """

    # Compute the total path
    path = os.path.join(dataset, path) if path != "-" else dataset

    # Attempt to open the file
    try:
        with open(path, "rb") as h:
            # Seek the correct position first
            h.seek(start)
            # Return it encoded
            return base64.b64encode(h.read(1 + end - start)).decode("UTF-8")
    except IOError as e:
        print(f"Failed to read file '{path}': {e}", file=sys.stderr)
        exit(1)





##### ENTRYPOINT #####
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <cat|cat_base64|cat_range|cat_range_base64>")
        exit(1)
    command = sys.argv[1]

    # Read the input arguments
    dataset = json.loads(os.environ["DATASET"])
    path    = json.loads(os.environ["NESTED_PATH"])

    # Run the function
    if command == "cat":
        # Don't forget to replace newlines with newlines with proper indentation, so YAML understands it's all the same file
        content = cat(dataset, path).replace("\n", "\n  ")
        print(f"output: |\n  {content}")
    elif command == "cat_base64":
        # Don't forget to replace newlines with newlines with proper indentation, so YAML understands it's all the same file
        content = cat_base64(dataset, path).replace("\n", "\n  ")
        print(f"output: |\n  {content}")
    elif command == "cat_range":
        # Also read the start and end now
        start = json.loads(os.environ["START"])
        end   = json.loads(os.environ["END"])

        # Don't forget to replace newlines with newlines with proper indentation, so YAML understands it's all the same file
        content = cat_range(dataset, path, start, end).replace("\n", "\n  ")
        print(f"output: |\n  {content}")
    elif command == "cat_range_base64":
        # Also read the start and end now
        start = int(os.environ["START"])
        end   = int(os.environ["END"])

        # Don't forget to replace newlines with newlines with proper indentation, so YAML understands it's all the same file
        content = cat_range_base64(dataset, path, start, end).replace("\n", "\n  ")
        print(f"output: |\n  {content}")
