# ************************************************************************ #
#                                                                          #
#                                                      :::      ::::::::   #
#  ft_different_errors.py                            :+:      :+:    :+:   #
#                                                  +:+ +:+         +:+     #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+        #
#                                              +#+#+#+#+#+   +#+           #
#  Created: 2026/05/15 21:36:49 by tokrabem        #+#    #+#              #
#  Updated: 2026/05/18 13:42:05 by tokrabem        ###   ########.fr       #
#                                                                          #
# ************************************************************************ #

print("=== Garden Error Types Demo ===")

def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        print("\nTesting operation 0...")
        input_data = int('abc')
        raise ValueError(input_data)
    if (operation_number == 1):
        print("Testing operation 1...")
        output = 25 / 0
        raise ZeroDivisionError(output)
    if (operation_number == 2):
        print("Testing operation 2...")
        file_open = open("/non/existent/file", "r")
        raise FileNotFoundError(file_open)
    if (operation_number == 3):
        print("Testing operation 3...")
        input1, input2 = "abc", 42
        raise TypeError(input1 + input2)
    if (operation_number == 4):
        print("Testing operation 4...")
        print("Operation completed successfully")

def test_error_types() -> None:
    i: int = 0
    while (i < 5):
        try:
            garden_operations(i)
        except ValueError as value_error:
            print(f"Caught ValueError: {value_error}")
        except ZeroDivisionError as div_error :
            print(f"Caught ZeroDivisionError: {div_error}")
        except FileNotFoundError as file_error:
            print(f"Caught FileNotFoundError: {file_error}")
        except TypeError as type_error:
            print(f"Caught TypeError: {type_error}")
        i += 1
    print("\nAll error types tested successfully!")

if __name__ == "__main__":
     test_error_types()