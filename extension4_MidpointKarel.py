"""
File: extension4_MidpointKarel.py
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
    """
    If on a n*n board, starting from (1 , 2), we put beepers to fill 1st Street in checkerboard pattern.
    There shall be n // 2 beepers on 1st Street. Midpoint shall be on n // 2 + 1
    e.g. 3*3 board: 3 // 2 = 1; 1 + 1 = 2 
         4*4 board: 4 // 2 = 2; 2 + 1 = 3
    We can fill 2nd Street with the same amount of beepers as n // 2, as our count marks. And mark midpoint with that.  
    """
    if not front_is_clear():  # When square is 1x1.
        put_beeper()
    else:
        move()
        if not front_is_clear():  # When square is 2x2.
            put_beeper()
        else:  # When square is larger than 2x2.
            turn_around()
            move()
            turn_around()  # Now back to (1, 1), facing east.
            checkerboard()
            count()
            mark_midpoint()


def checkerboard():
    """
    Pre-condition: Karel's at (1, 1), facing east. There's no beeper on 1st Street.
    Post-condition: Karel's at (1, 1), facing east. Starting from (1, 2), 1st Street's filled in checkerboard pattern.
    """
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()
    turn_around()
    while front_is_clear():
        move()
    turn_around()  # Back to (1, 1) facing east


def count():
    """
    Pre-condition: Karel's at (1, 1), facing east. Starting from (1, 2), 1st Street's filled in checkerboard pattern.
    Post-condition: Karel's at (2, 1), facing east. 2nd Street has same amount of beepers
    as 1st Street used to have in pre-condition.
    """
    while not on_beeper() and front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
            turn_left()
            move()
            turn_left()  # Now on 2nd Street, facing west
            while not on_beeper() and front_is_clear():
                move()
                if on_beeper():
                    turn_around()
                    move()
                    put_beeper()  # Put a count mark.
                    turn_right()
                    move()  # Now on 1st street, facing south, so that we can leave this loop.
                elif not front_is_clear():
                    put_beeper()  # This is the first count mark put on 2nd Street.
                    turn_around()
                    move()
                    turn_right()
                    move()  # Now on 1st street, facing south, so that we can leave this loop.
            turn_left()
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()  # Now on (2, 1), facing east.


def mark_midpoint():
    """
    Pre-condition: Karel's at (2, 1), facing east. 2nd Street has same amount of beepers
    as 1st Street used to have in pre-condition.
    Post-condition: Karel is on the midpoint. The midpoint beeper is put on 1st Street.
    """
    while on_beeper():
        pick_beeper()
        move()
    turn_right()  # Now at n // 2 + 1, facing south.
    while front_is_clear():
        move()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
