# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_raise_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/15 20:44:49 by tokrabem        #+#    #+#               #
#  Updated: 2026/07/07 16:37:25 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if (temp < 0):
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    if (temp > 40):
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")
    return (temp)


def test_temperature() -> None:
    try:
        input_data = '25'
        print(f"\nInput data is {input_data!r}")
        print(f"Temperature is now {input_temperature(input_data)}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    try:
        input_data = 'abc'
        print(f"\nInput data is {input_data!r}")
        print(f"Temperature is now {input_temperature(input_data)}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    try:
        input_data = '100'
        print(f"\nInput data is {input_data!r}")
        print(f"Temperature is now {input_temperature(input_data)}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    try:
        input_data = '-50'
        print(f"\nInput data is {input_data!r}")
        print(f"Temperature is now {input_temperature(input_data)}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden temperature ===")
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
