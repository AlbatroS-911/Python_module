# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/15 20:44:49 by tokrabem        #+#    #+#               #
#  Updated: 2026/07/06 17:42:59 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if (temp < 0):
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    if (temp > 40):
        raise Exception(f"{temp}°C is too hot for the plants (max 40°C)")
    return (temp)


def test_temperature(test: str) -> None:
    try:
        print(f"Input data is {test!r}")
        converted_data = input_temperature(test)
        print(f"Temperature is now {converted_data}°C")
    except Exception as error_exception:
        print(f"Caught input_temperature error: {error_exception}")
    print()


if __name__ == "__main__":
    print("=== Garden temperature ===\n")
    test_temperature("25")
    test_temperature("abc")
    test_temperature("100")
    test_temperature("-50")
    print("All tests completed - program didn\'t crash!")
