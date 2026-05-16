# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/15 20:44:49 by tokrabem        #+#    #+#               #
#  Updated: 2026/05/16 07:10:09 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== Garden temperature ===\n")


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if (temp < 0):
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    if (temp > 40):
        raise Exception(f"{temp}°C is too hot for the plants (max 40°C)")
    return (temp)


def test_temperature() -> None:
    input_data = 'lkj'
    try:
        converted_data = input_temperature(input_data)
        try:
            print(f"Input data is '{converted_data}'")
            print(f"Temperature is now {converted_data}°C")
        except Exception as error:
            print(f"Input data is '{converted_data}'")
            print("Caught input_temperature error:", error)

    except Exception as error_exception:
        print(f"Input data '{input_data}'")
        print("Caught input_temperature error: ", error_exception)
    print("\nAll tests completed - program didn\'t crash!")


if __name__ == "__main__":
    test_temperature()
