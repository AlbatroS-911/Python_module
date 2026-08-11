from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: list[typing.Any] = []
        self._processed = 0
        self._output_count: int = 0

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
        count = self._output_count
        self._output_count += 1
        return (count, str(item))


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
            return all(isinstance(i, (int, float))
                       for i in data
                       )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper numeric data")
        if isinstance(data, (list, tuple)):
            for item in data:
                self.data.append(str(item))
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
            raise Exception("Got exception: Improper dict data")
        if isinstance(data, (list, tuple)):
            for d in data:
                self.data.append(self._str_conversion(d))
            self._processed += len(data)
        else:
            self.data.append(self._str_conversion(data))
            self._processed += 1


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        csv = ",".join(value for i, value in data)
        print("CSV Output:")
        print(f"{csv}")


class JSONExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        json = ", ".join(f'"item_{i}": "{value}"' for i, value in data)
        print("JSON Output:")
        print(f"{{{json}}}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self._processors:
            registered: list[tuple[int, str]] = []
            for i in range(nb):
                try:
                    result = processor.output()
                    registered.append(result)
                except IndexError:
                    break
            plugin.process_output(registered)


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Initialize Data Stream...")
    DataStream().print_processors_stats()
    print()
    stream1: list[typing.Any] = ['Hello world', [3.14, -1, 2.71],
                                 [{'log_level': 'WARNING',
                                  'log_message':
                                   'Telnet access! Use ssh instead'},
                                 {'log_level': 'INFO',
                                  'log_message': 'User wil is connected'}],
                                 42, ['Hi', 'five']]
    data_stream: DataStream = DataStream()
    num_proc: DataProcessor = NumericProcessor()
    text_proc: DataProcessor = TextProcessor()
    log_proc: DataProcessor = LogProcessor()
    print("Registering Processors")
    print(f"Send first batch of data on stream: {stream1}")
    print()
    data_stream.register_processor(num_proc)
    data_stream.register_processor(text_proc)
    data_stream.register_processor(log_proc)
    data_stream.process_stream(stream1)
    data_stream.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    try:
        data_stream.output_pipeline(3, CSVExportPlugin())
    except Exception as err:
        print(f" CSV pipeline error: {err}")
    print()
    data_stream.print_processors_stats()
    print()
    stream2: list[typing.Any] = [21, ['I love AI', 'LLMs are wonderful',
                                      'Stay healthy'],
                                 [{'log_level': 'ERROR',
                                   'log_message': '500 server crash'},
                                  {'log_level': 'NOTICE',
                                   'log_message':
                                   'Certificate expires in 10 days'}],
                                 [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"Send another batch of data: {stream2}")
    print()
    data_stream.process_stream(stream2)
    data_stream.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    try:
        data_stream.output_pipeline(5, JSONExportPlugin())
    except Exception as err:
        print(f" JSON pipeline error: {err}")
    print()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
