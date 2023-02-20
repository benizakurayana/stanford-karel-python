"""
File: MidpointKarel.py
Name: Jane
----------------------------
This program shows Karel leaving a beeper on the corner closest to the center of 1st Street, or either of
the two central corners if 1st Street has an even number of corners. We call it the "midpoint."
The world may be of any size, but it is as tall as it is wide (a square).
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: There's no beeper.
    Post-condition: One beeper is on the midpoint of 1st Street.
    """
    put_beeper()  # The very first beeper put
    while front_is_clear():
        move()
    put_beeper()  # The second beeper put
    turn_around()
    while front_is_clear():  # Karel goes between left and right sides and taking the beepers closer to each other.
        move()
        if on_beeper():
            pick_beeper()
            turn_around()
            move()
            put_beeper()
            """
            In the last iteration of this loop, two beepers will be on the same point (midpoint).
            """
    turn_around()
    while not on_beeper():
        move()
    pick_beeper()  # So that only one beeper is left on the midpoint.


def turn_around():
    for i in range(2):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
