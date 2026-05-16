# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_first_exception.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/15 18:57:44 by tokrabem        #+#    #+#               #
#  Updated: 2026/05/15 20:46:08 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

print("=== Garden temperature ===\n")


def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    input_data = '25'
    try:
        print(f"Input data is '{input_temperature(input_data)}'")
        print(f"Temperature is now {input_temperature(input_data)}°C")

    except Exception as e:
        print(f"Input data '{input_data}'")
        print("Caught input_temperature error: ", e)
    print("\nAll tests completed - program didn\'t crash!")


if __name__ == "__main__":
    test_temperature()
