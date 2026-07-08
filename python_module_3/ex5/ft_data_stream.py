# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/26 21:04:13 by tokrabem        #+#    #+#               #
#  Updated: 2026/07/08 08:35:54 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random
import typing

print("=== Game Data Stream Processor ===")


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    name: list[str] = ['Charlie', 'Bob', 'Alice', 'Dylan']
    action: list[str] = ['run', 'eat', 'sleep', 'grab', 'move', 'sleep',
                         'swim', 'climb', 'release', 'use']
    while True:
        yield (random.choice(name), random.choice(action))


def consume_event(
        event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        index: int = random.randrange(len(event_list))
        picked_one = event_list[index]
        del event_list[index]
        yield picked_one


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print()
    first_event = gen_event()
    for i in range(1000):
        (name, action) = next(first_event)
        print(f"Event {i}: Player {name} did action {action}")
    second_event = gen_event()
    new_event_list: list[tuple[str, str]] = []
    for i in range(10):
        new_event_list += [next(second_event)]
    print(f"Built list of 10 events: {new_event_list}")
    for event in consume_event(new_event_list):
        print(f"Got event form list: {event}")
        print(f"Remains in list: {new_event_list}")
