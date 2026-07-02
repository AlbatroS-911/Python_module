# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_processor.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: toky <toky@student.42.fr>                 +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/03 08:24:34 by tokrabem        #+#    #+#               #
#  Updated: 2026/07/02 07:13:35 by toky            ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from abc import ABC, abstractmethod
from typing import Any

# Number = Union[int, float]
class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: Any = None

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return (len(self.data), str(self.data))


class NumericProcessor(DataProcessor):

    def __init__(self) -> None:
        super().__init__()
        self.data: list[int | float] = []
         
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, (list, tuple)):
            return all (isinstance(i, (int, float))
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
            


# class TextProcessor(DataProcessor):
#     def validate(self, data: Any) -> builtins.bool:
#         return super().validate(data)
    
#     def ingest(self, data: Any) -> None:
#         return super().ingest(data)


# class LogProcessor(DataProcessor):
#     def validate(self, data: Any) -> builtins.bool:
#         return super().validate(data)
    
#     def ingest(self, data: Any) -> None:
#         return super().ingest(data)

if __name__ == "__main__": 
    print("=== Code Nexus - Data Processor ===")
    print()
    num_data = NumericProcessor()
    print("Testing Numeric Processor...")
    print(f"Trying to validate input 'list': {num_data.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_data.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        (num_data.ingest('foo'))
    except Exception as err:
        print(err)
    print("Processing data: [1, 2, 3, 4, 5]")
    num_data.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for value in range (3):
        print(f"Numeric value {value}: {num_data.data[value]}")
    