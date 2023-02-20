"""
File: CollectNewspaperKarel.py
Name: Jane
--------------------------------
This program shows Karel, whose initial position is in the upper left corner of its house
(at Street 4, Avenue 3, in short: (4, 3)),
walking to the door of the house at (3, 6),
picking up the newspaper, represented by a beeper,
returning to its initial position (4, 3), and dropping the newspaper down.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at (4, 3), facing east, and the beeper is at (3, 6).
    Post-condition: Karel and beeper are at (4, 3) and Karel is facing east.
    """
    move_to_newspaper()
    bring_newspaper_home()


def move_to_newspaper():
    """
    Pre-condition: Karel is at (4, 3), facing east, and the beeper is at (3, 6).
    Post-condition: Karel is at (3, 6), facing east, with the beeper picked up.
    """
    turn_right()
    move()
    turn_left()
    for i in range(3):
        move()
    pick_beeper()


def bring_newspaper_home():
    """
    Pre-condition: Karel is at (3, 6), facing east, with the beeper picked up.
    Post-condition: Karel and beeper are at (4, 3) and Karel is facing east.
    """
    for i in range(2):
        turn_left()
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
