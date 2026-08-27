#!/usr/bin/env python3

import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
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
            print(f"File '{file_name}' closed.\n")

            print("Transform data:")
            print("---\n")
            new_content = ""
            for char in content:
                if char == "\n":
                    new_content += "#\n"
                else:
                    new_content += char
            print(new_content)
            print("---")
            new_name = input("Enter new file name (or empty):")
            if new_name:
                file = open(new_name, "w")
                print(f"Saving data to '{new_name}'")
                file.write(new_content)
                print(f"Data saved in file '{new_name}'")
                file.close()
            else:
                print("Not saving data.")

        except FileNotFoundError as e:
            print(f"Error opening file '{file_name}': {e}")


if __name__ == "__main__":
    main()
