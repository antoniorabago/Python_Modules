#!/usr/bin/env python3

from abc import ABC, abstractmethod
import typing
from typing import Any, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[Any] = []
        self._output_count = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        value: str = ""
        count: int = 0
        if self._data:
            count = self._output_count
            value = self._data[0]
            self._output_count += 1
            self._data.pop(0)
        return count, value


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            processed = False
            for processor in self.processors:
                if processor.validate(item):
                    processor.ingest(item)
                    processed = True
                    break
            if not processed:
                print(f"DataStream error - Can't process element in stream: "
                      f"{item}")

    def print_processors_stats(self) -> None:
        if self.processors:
            for processor in self.processors:
                name = processor.__class__.__name__.replace("Processor",
                                                            " Processor")
                total = processor._output_count + len(processor._data)
                remaining = len(processor._data)
                print(f"{name}: total {total} items processed, "
                      f"remaining {remaining} on processor")
        else:
            print("No processor found, no data\n")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if self.processors:
            for processor in self.processors:
                data: list[tuple[int, str]] = []
                for _ in range(nb):
                    if not processor._data:
                        break
                    output_item: tuple[int, str] = processor.output()
                    data.append(output_item)
                if data:
                    plugin.process_output(data)


class CSVExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        csv_items: list[str] = []
        for _, value in data:
            csv_items.append(value)
        print("CSV Output")
        print(",".join(csv_items))


class JSONExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json_items: list[str] = []
        for index, value in data:
            json_items.append(f'"item_{index}": "{value}"')
        print("JSON Output")
        print("{" + ", ".join(json_items) + "}")


def main() -> None:
    print("=== Code Nexus- Data Pipeline ===")
    print("Initialize Data Stream...\n")
    print("== DataStream statistics ==")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("Registering Processors")
    numeric = NumericProcessor()
    data_stream.register_processor(numeric)
    text = TextProcessor()
    data_stream.register_processor(text)
    log = LogProcessor()
    data_stream.register_processor(log)

    data = ['Hello world',
            [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
              'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
            42,
            ['Hi', 'five']]
    print(f"Send first batch of data on stream: {data}")
    data_stream.process_stream(data)

    print("== DataStream statistics ==")
    data_stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csvplugin = CSVExport()
    data_stream.output_pipeline(3, csvplugin)

    print("\n== DataStream statistics ==")
    data_stream.print_processors_stats()

    data = [21,
            ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
            [{'log_level': 'ERROR',
              'log_message': '500 server crash'},
             {'log_level': 'NOTICE',
              'log_message': 'Certificate expires in 10 days'}],
            [32, 42, 64, 84, 128, 168],
            'World hello']
    print(f"\nSend another batch of data: {data}")
    print("\n== DataStream statistics ==")
    data_stream.process_stream(data)
    data_stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    jsonplugin = JSONExport()
    data_stream.output_pipeline(5, jsonplugin)

    print("\n== DataStream statistics ==")
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
