#!/usr/bin/env python3
"""
Author : Bonnie
Date   : 2025-02-12
Purpose: say hello
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="say hello", 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-g",
        "--greeting",
        help="A greeting to use",
        metavar="str",
        type=str,
        default="Howdy",
    )

    parser.add_argument(
        "-n",
        "--name",
        help="A name to greet",
        metavar="str",
        type=str,
        default="Stranger",
    )

    parser.add_argument(
        "-e", "--excited", 
        help="Print ! if this flag is present", 
        action="store_true"
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    greeting = args.greeting
    name = args.name
    excited = args.excited
    if excited:
        print(f"{greeting}, {name}!")
    else:
        print(f"{greeting}, {name}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
