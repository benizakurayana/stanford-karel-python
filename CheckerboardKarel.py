"""
File: CheckerboardKarel.py
Name: Jane
----------------------------
This program shows Karel drawing a checkerboard pattern using beepers on any square or rectangular boards.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at (1, 1) and the board is empty.
    Post-condition: The board is filled in checkerboard patter.
    """
    """
    Geometrically, every square is a rectangle. An algorithm that works on a rectangle board shall 
    also work on a square one.
    However, there are two types of rectangles. They have different checkerboard patterns.
    Type 1: length of the bottom side is an odd number. 
    Type 2: length of the bottom side is an even number.
    They will need different algorithm.
    """
    put_one_line_a()
    """
    We can determine which type the rectangle is by letting Karel fill up the bottom side.
    If Karel ends up stepping on a beeper, it's Type 1. Otherwise, Type 2.
    For both types, we let Karel continue to fill the board from bottom to top in a route of S shape, 
    however, with different methods to fill beepers. 
    """
    if on_beeper():
        """
        Rectangle: Type 1
        Filling method: B -> A -> B -> A
        """
        while left_is_clear():
            if left_is_clear():  # Check if top side reached.
                turn_left()
                move()
                turn_left()
                put_one_line_b()
                if right_is_clear():  # Check if top side reached.
                    turn_right()
                    move()
                    turn_right()
                    put_one_line_a()
                else:
                    turn_right()
    else:
        """
        Rectangle: Type 2
        Filling method: A -> A -> A -> A 
        """
        while left_is_clear():
            if left_is_clear():  # Check if top side reached.
                turn_left()
                move()
                turn_left()
                put_one_line_a()
                if right_is_clear():  # Check if top side reached.
                    turn_right()
                    move()
                    turn_right()
                    put_one_line_a()
                else:
                    turn_right()


def put_one_line_a():
    """
    Filling method A
    Put. Loop: check front, move, check front, move, put
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def put_one_line_b():
    """
    Filling method B
    Loop: move, put, check front, move
    """
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
