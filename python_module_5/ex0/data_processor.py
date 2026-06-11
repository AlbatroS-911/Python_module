# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  data_processor.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/03 08:24:34 by tokrabem        #+#    #+#               #
#  Updated: 2026/06/05 11:06:14 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import abc
from typing import Any
import builtins


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def validate(self, data: Any) -> builtins.bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    # def output(self) -> tuple[int, str]:
    #     return ()


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
    
    def validate(self, data: Any) -> bool:
        super().validate(data)
        if data is (int or float):
            return (True)
        return (False)
    

    def ingest(self, data: Any) -> None:
        return super().ingest(data)


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
    fuck = NumericProcessor().validate(1)
    print()