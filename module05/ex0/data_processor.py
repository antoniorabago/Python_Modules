#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[Any] = []
        self._index = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        value: str = ""
        index: int = 0
        if self._data:
            index = self._index
            value = self._data[0]
            self._index += 1
            self._data.pop(0)
        return index, value


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._data.append(str(item))
        else:
            self._data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._data.append(item)
        else:
            self._data.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str):
                    return False
                if not isinstance(value, str):
                    return False
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False
                for key, value in item.items():
                    if not isinstance(key, str):
                        return False
                    if not isinstance(value, str):
                        return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                self._data.append(f"{item['log_level']}: "
                                  f"{item['log_message']}")
        else:
            self._data.append(f"{data['log_level']}: {data['log_message']}")


def main() -> None:
    print("=== Code Nexus- Data Processor ===\n")
    print("Testing Numeric Processor...")
    numeric = NumericProcessor()
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")
    list_numeric: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {list_numeric}")
    numeric.ingest(list_numeric)
    print("Extracting 3 values..")
    for _ in range(3):
        index, value = numeric.output()
        print(f"Numeric value {index}: {value}")

    print("\nTesting Text Processor...")
    text = TextProcessor()
    print(f"Trying to validate input '42': {text.validate(42)}")
    list_text: list[str] = ["Hello", "Nexus", "World"]
    print(f"Processing data: {list_text}")
    text.ingest(list_text)
    print("Extracting 1 value...")
    index, value = text.output()
    print(f"Text value {index}: {value}")

    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    dict_log: list[dict[str, str]] = [{'log_level': 'NOTICE', 'log_message':
                                       'Connection to server'},
                                      {'log_level': 'ERROR', 'log_message':
                                       'Unauthorized access!!'}]
    log.ingest(dict_log)
    print("Extracting 2 values...")
    for _ in range(2):
        entry, value = log.output()
        print(f"Log entry {entry}: {value}")


if __name__ == "__main__":
    main()
