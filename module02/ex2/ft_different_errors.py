#!/usr/bin/env python3

def garden_operations(operation_number: int) -> float:
    result: float = 0.0
    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        result = 1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "campus" + 42
    return result


def test_error_types() -> None:
    for operation in range(5):
        print(f"Testing operation {operation}...")
        try:
            garden_operations(operation)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        else:
            print("Operation completed successfully \n")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("All tests completed - program didn't crash")


if __name__ == "__main__":
    main()
