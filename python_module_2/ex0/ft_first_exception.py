# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/15 18:57:44 by tokrabem        #+#    #+#               #
#  Updated: 2026/05/19 11:28:42 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== Garden temperature ===")


def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    try:
        input_data = '25'
        print(f"\nInput data is '{input_temperature(input_data)}'")
        print(f"Temperature is now {input_temperature(input_data)}°C")
    except Exception as e:
        print("Caught input_temperature error: ", e)
    try:
        input_data = 'abc'
        print(f"\nInput data is '{input_data}'")
        print(f"Temperature is now {input_temperature(input_data)}°C")
    except Exception as e:
        print("Caught input_temperature error: ", e)
    print("\nAll tests completed - program didn\'t crash!")

if __name__ == "__main__":
    test_temperature()
