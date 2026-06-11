# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_achievement_tracker.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: tokrabem <tokrabem@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/05/20 18:17:09 by tokrabem        #+#    #+#               #
#  Updated: 2026/05/26 17:07:32 by tokrabem        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import random

print("=== Achievement Tracker System ===\n")


def all_achievements() -> list[str]:
    return [
        'Crafting Genius',
        'Strategist',
        'World Savior',
        'Speed Runner',
        'Survivor',
        'Master Explorer',
        'Treasure Hunter',
        'Unstoppable',
        'First Steps',
        'Collector Supreme',
        'Untouchable',
        'Sharp Mind',
        'Boss Slayer',
        'Hidden Path Finder'
    ]


def gen_player_achievements() -> set[str]:
    achievements_types = all_achievements()

    count = random.randint(3, len(achievements_types))
    achievement = random.sample(achievements_types, count)
    return set(achievement)


if __name__ == "__main__":
    a = gen_player_achievements()
    b = gen_player_achievements()
    c = gen_player_achievements()
    d = gen_player_achievements()
    players = {"Alice": a, "Bob": b, "Charlie": c, "Dylan": d}
    for key in players:
        print(f"Player {key}: {players[key]}")
    print(f"\nAll distinct achievements: {a | b | c | d}")
    print(f"\nCommon achievements: {a & b & c & d}")
    for key in players:
        other = set.union(*[players[k] for k in players if k != key])
        print(f"\nOnly {key} has: {players[key] - (other)}")
    achievements: list[str] = all_achievements()
    print('\n')
    for key in players:
        print(f"{key} is missing: {set(achievements) - (players[key])}")
