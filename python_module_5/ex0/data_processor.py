
from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[typing.Any] = []

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data:
            raise IndexError("No data in the processor...")
        item = self.data.pop(0)
        return (1, str(item))


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()
        self.data = []

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, (list, tuple)):
            return all(isinstance(i, (int, float)) and not isinstance(i, bool)
                       for i in data
                       )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception(" Got exception: Improper numeric data")
        if isinstance(data, (list, tuple)):
            for item in data:
                self.data.append(str(item))
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
            raise Exception(" Got exception: Improper text data")
        if isinstance(data, (list, tuple)):
            self.data.extend(data)
        else:
            self.data.append(data)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.data: list[str] = []

    def _str_conversion(self, d: dict[str, str]) -> str:
        return f"{d['log_level']}: {d['log_message']}"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return True
        if isinstance(data, (list, tuple)):
            return all(isinstance(i, dict)
                       for i in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception(" Got exception: Improper dict data")
        if isinstance(data, (list, tuple)):
            for d in data:
                self.data.append(self._str_conversion(d))
        else:
            self.data.append(self._str_conversion(data))


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    num_data = NumericProcessor()
    print("Testing Numeric Processor...")
    print(f" Trying to validate input '42': {num_data.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_data.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_data.ingest('foo')
    except Exception as err:
        print(err)
    num_test: list[int | float] = [1, 2, 3]
    print(num_data.validate(num_test))
    num_data.ingest(num_test)
    count, value = num_data.output()
    print(f"{count}, {value}")
    print(f" Processing data: {num_test}")
    try:
        num_data.ingest(num_test)
    except Exception as err:
        print(err)
    print(" Extracting 3 values...")
    try:
        for i in range(3):
            count, value = num_data.output()
            print(f" Numeric value {i}: {value}")
    except IndexError:
        print(" An invalid data detected...")
    print()
    print("Testing Text Processor...")
    str_data = TextProcessor()
    print(f" Trying to validate input '42': {str_data.validate(42)}")
    str_test: list[str] = ['Hello', "Nexus", 'World']
    print(f" Processing data: {str_test}")
    try:
        str_data.ingest(str_test)
    except Exception as err:
        print(err)
    print(" Exctracting 1 value...")
    try:
        count, value = str_data.output()
        print(f" Text value {count - 1}: {value}")
    except IndexError as err:
        print(err)
    print()
    print("Testing Log Processor...")
    log_data = LogProcessor()
    print(f" Trying to validate input 'Hello': {log_data.validate('Hello')}")
    log_test: list[dict[str, str]] = [{'log_level': 'NOTICE',
                                       'log_message': 'Connection to server'},
                                      {'log_level': 'ERROR',
                                       'log_message': 'Unauthorized access!!'}]
    print(f" Processing data: {log_test}")
    try:
        log_data.ingest(log_test)
    except Exception as err:
        print(err)
    print(" Extracting 2 values...")
    for i in range(2):
        try:
            count, value = log_data.output()
            print(f" Log entry {i}: {value}")
        except IndexError:
            print(" An invalid data detected...")


if __name__ == "__main__":
    main()
