
from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: typing.Any = None
        self._processed = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str] | None:
        if not self.data:
            return None
        item = self.data.pop(0)
        return (1, str(item))


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()
        self.data: list[int | float] = []

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, (list, tuple)):
            return all(isinstance(i, (int, float))
                       for i in data
                       )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper numeric data")
        if isinstance(data, (list, tuple)):
            self.data.extend(data)
            self._processed += len(data)
        else:
            self.data.append(data)
            self._processed += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.data: list[str] = []

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, (list, tuple)):
            return all(isinstance(i, str)
                       for i in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper text data")
        if isinstance(data, (list, tuple)):
            self.data.extend(data)
            self._processed += len(data)
        else:
            self.data.append(data)
            self._processed += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.data: list[dict[str, str]] = []

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return True
        if isinstance(data, (list, tuple)):
            return all(isinstance(i, dict)
                       for i in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper dict data")
        if isinstance(data, (list, tuple)):
            self.data.extend(data)
            self._processed += len(data)
        else:
            self.data.append(data)
            self._processed += 1


class DataStream():
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for data in stream:
            handled: bool = False
            for processor in self._processors:
                if processor.validate(data):
                    try:
                        processor.ingest(data)
                        handled = True
                    except Exception:
                        print("Error in ingestion")
                    break
            if not handled:
                print(
                    f"DataStream error -"
                    f"Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
        for processor in self._processors:
            name = type(processor).__name__
            formatted = "".join(
                f" {letter}" if letter.isupper() and i > 0 else letter
                for i, letter in enumerate(name)
            )
            total = processor._processed
            remaining = len(processor.data)
            print(
                f"{formatted}: total {total} items processed, "
                f"remaining {remaining} on processor")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Initialize Data Stream...")
    DataStream().print_processors_stats()
    print()
    stream: list[typing.Any] = ['Hello world', [3.14, -1, 2.71],
                                [{'log_level': 'WARNING',
                                  'log_message':
                                  'Telnet access! Use ssh instead'},
                                 {'log_level': 'INFO',
                                  'log_message': 'User wil is connected'}],
                                42, ['Hi', 'five']]
    data_stream: DataStream = DataStream()
    num_proc: NumericProcessor = NumericProcessor()
    print("Registering Numeric Processor")
    print()
    print(f"Sending first batch of data on stream : {stream}")
    data_stream.register_processor(num_proc)
    data_stream.process_stream(stream)
    data_stream.print_processors_stats()
    print()
    print("Registering other data processors")
    print("Send the same batch again")
    text_proc: TextProcessor = TextProcessor()
    log_proc: LogProcessor = LogProcessor()
    data_stream.register_processor(text_proc)
    data_stream.register_processor(log_proc)
    data_stream.process_stream(stream)
    data_stream.print_processors_stats()
    print()
    print("Consume some elements from the data processors:"
          " Numeric 3, Text 2, Log 1")
    for i in range(3):
        num_proc.output()
    for i in range(2):
        text_proc.output()
    for i in range(1):
        log_proc.output()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
