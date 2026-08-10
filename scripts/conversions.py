#!/usr/bin/env python3

import argparse

def main():
    # Parser Init
    parser = argparse.ArgumentParser(description='Convert Binary, Decimal, and\
                                     Hexadecimal values.')
    parser.add_argument(
        '-t', choices=['binary', 'decimal', 'hexadecimal'],
        required=True, type=str)

    parser.add_argument('-o', choices=['binary', 'decimal','hexadecimal'],
                        required=True, type=str)

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
    print(args)
