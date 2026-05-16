# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_different_errors.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/15 21:36:49 by tokrabem        #+#    #+#               #
#  Updated: 2026/05/16 08:28:47 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== Garden Error Types Demo ===")

def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        print("Testing operation 0...")
        try:
            input = int('abc')
            raise ValueError(input)
        except ValueError as err:
            print("Caught ValueError:", err)
    elif (operation_number == 1):
        print("Testing operation 1...")
        try:
            output = 25 / 0
            raise ZeroDivisionError(output)
        except ZeroDivisionError as div_error:
            print("Caught ZeroDivisionError:", div_error)
    elif (operation_number == 2):
        print("Testing operation 2...")
        try:
            file_open = open('/non/existent/file', 'r')
            raise FileNotFoundError(file_open)
        except FileNotFoundError as file_error:
            print("Caught FileNotFoundError:", file_error)
    elif (operation_number == 3):
        print("Testing operation 3...")
        try:
            input1, input2 = 'a', 42
            raise TypeError(int(input1) + input2)
        except TypeError as type_error:
            print("Caught TypeError:", type_error)
    else:
        print("Testing operation 4...")
        print("Operation completed successfully")
        


if __name__ == "__main__":
     garden_operations(3)