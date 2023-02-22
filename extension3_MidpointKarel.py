"""
File: extension3_MidpointKarel.py
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
    If starting from (1, 1) we let Karel draw with beepers a counterclockwise square_spiral from outer side, 
    the last beeper put shall be the center of the square.
    This works on both of the following types of board:
    - Type 1: A board with even number of corners. When the last one is put, karel is facing west.
    - Type 2: A board with odd number of corners. When the last one is put, karel is facing east.
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
            square_spiral()
            clear_all()
            mark_midpoint()


def square_spiral():
    """
    Pre-condition: Karel is at (1, 1), facing east. There's no beeper on the board.
    Post-condition: The board is filled with beepers.
                    Karel is either at top right corner facing south, or at bottom right corner facing north.
    """
    while front_is_clear() and not on_beeper():
        put_beeper()
        move()
        if on_beeper():  # If there's a beeper in the front of Karel, Karel shall return and go to his left.
            turn_around()
            move()
            turn_right()
            move()
            if not on_beeper():  # If no beeper on his left, he does nothing and the loop will start from the beginning.
                pass
            if on_beeper():
                """
                If there's a beeper in the front of Karel and there's also another one on his left, 
                it means it's the center.
                """
                turn_around()
                move()
                put_beeper()  # Now back to the center and put a beeper.
                if facing_north():  # even number
                    while front_is_clear():
                        move()
                    turn_right()
                    while front_is_clear():
                        move()
                    turn_right()
                else:  # odd number
                    while front_is_clear():
                        move()
                    turn_left()
                    while front_is_clear():
                        move()
                    turn_left()
        elif not front_is_clear():  # In the first round of the spiral, Karel might meet the walls.
            put_beeper()
            turn_left()
            move()


def clear_all():
    """
    Pre-condition: The board is filled with beepers. The board is filled with beepers.
                    Karel is either at top right corner facing south, or at bottom right corner facing north.
    Post-condition: Only the center beep is left on the board. Karel is at top left corner facing south.
    """
    while front_is_clear():
        pick_beeper()
        move()
        if not front_is_clear():
            """
            When Karel makes one move, we have to check if he meets the bottom or top side 
            of the square and let him go to the next avenue.
            """
            if on_beeper():
                pick_beeper()
            if facing_south():
                if right_is_clear():
                    turn_right()
                    move()
                    turn_right()
            else:
                if left_is_clear():
                    turn_left()
                    move()
                    turn_left()
    turn_around()


def mark_midpoint():
    """
    Pre-condition: Only the center beep is left on the board. Karel is at top left corner facing south.
    Post-condition: The midpoint beeper is put on 1st Street.
                    Karel is either at top right corner facing north, or at bottom right corner facing south.
    """
    while front_is_clear():
        if on_beeper():  # When Karel finds the only beeper left.
            pick_beeper()
            if facing_north():
                turn_around()  # Face south
            while front_is_clear():
                move()
            put_beeper()  # Put the beeper on 1st Street.

        else:
            move()
        if not front_is_clear():
            """
            When Karel makes one move, we have to check if he meets the bottom or top side 
            of the square and let him go to the next avenue.
            """
            if facing_north():
                if right_is_clear():
                    turn_right()
                    move()
                    turn_right()
            else:
                if left_is_clear():
                    turn_left()
                    move()
                    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
