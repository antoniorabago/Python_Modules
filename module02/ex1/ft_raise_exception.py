#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int: int
    temp_int = int(temp_str)
    if temp_int > 40:
        raise ValueError(f"{temp_int} °C is too hot for plants (max 40°C)")
    elif temp_int < 0:
        raise ValueError(f"{temp_int} °C is too cold for plants (min 0°C)")
    return temp_int


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        print(f"Temperature is now {input_temperature('25')}º\n")
        print("Input data is 'abc'")
        print(f"Temperature is now {input_temperature('abc')}º\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e} \n")

    try:
        print("Input data is '100'")
        print(f"Temperature is now {input_temperature('100')}º\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e} \n")

    try:
        print("Input data is '-50'")
        print(f"Temperature is now {input_temperature('-50')}º\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e} \n")


def main() -> None:
    print("=== Garden Temperature Checker === \n")
    test_temperature()
    print("All tests completed - program didn't crash")


if __name__ == "__main__":
    main()
