#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int: int
    temp_int = int(temp_str)
    return temp_int


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        print(f"Temperature is now {input_temperature('25')}º\n")
        print("Input data is 'abc'")
        print(f"Temperature is now {input_temperature('abc')}º\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e} \n")


def main() -> None:
    print("=== Garden Temperature === \n")
    test_temperature()
    print("All tests completed - program didn't crash")


if __name__ == "__main__":
    main()
