
from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: typing.Any = None

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str] | None:
        if not self.data:
            return None
        return (len(self.data), str(self.data))


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
        else:
            self.data.append(data)


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
        else:
            self.data.append(data)


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
        else:
            self.data.append(data)


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    num_data = NumericProcessor()
    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {num_data.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_data.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_data.ingest('foo')
    except Exception as err:
        print(err)
    num_test: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_test}")
    num_data.ingest(num_test)
    print("Extracting 3 values...")
    for value in range(3):
        print(f"Numeric value {value}: {num_data.data[value]}")
    print()
    print("Testing Log Processor...")
    str_data = TextProcessor()
    print(f"Trying to validate input '42': {str_data.validate(42)}")
    print("Testing of invalid data without validation:")
    str_test: list[str] = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {str_test}")
    str_data.ingest(str_test)
    print("Exctracting 1 value...")
    print(f"Text value 0: {str_data.data[0]}")
    print()
    print("Testing Log Processor...")
    log_data = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_data.validate('Hello')}")
    log_test: list[dict[str, str]] = [{'log_level': 'NOTICE',
                                       'log_message': 'Connection to server'},
                                      {'log_level': 'ERROR',
                                       'log_message': 'Unauthorized access!!'}]
    print(f"Processing data: {log_test}")
    log_data.ingest(log_test)
    print("Extracting 2 values...")
    for i, d in enumerate(log_data.data[0:]):
        if "log_level" and "log_message" in d:
            print(
                f"Log entry {i}: {d.get('log_level')}: {d.get('log_message')}")


if __name__ == "__main__":
    main()
