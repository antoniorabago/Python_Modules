#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        file_name = sys.argv[1]
        print(f"Accessing file '{file_name}'")
        try:
            file = open(file_name, "r")
            content = file.read()
            print("---\n")
            print(content)
            print("---")
            file.close()
            print(f"File '{file_name}' closed.")
        except FileNotFoundError as e:
            print(f"Error opening file '{file_name}': {e}")


if __name__ == "__main__":
    main()
