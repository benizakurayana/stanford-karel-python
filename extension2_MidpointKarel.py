"""
File: extension2_MidpointKarel.py
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
    There are two types of boards in this problem:
    - Type 1: A board with even number of corners.
    - Type 2: A board with odd number of corners.
    If starting from (1, 1), we draw pyramid pattern with beepers, starting from 1st Street as the bottom, 
    the peak point of the pyramid shall be the center of the square, and thus we can mark the midpoint with it.   
    It works on Type 2 well. However, not on Type 1 because we won't be able to put a beeper on the peak point.
    We need to adjust our algorithm a bit. First, we draw checkerboard pattern on 1st Street. 
    And we draw small triangles from right to left, bottom to top to form a pyramid pattern. 
    So that our algorithm can work on both Type 1 and 2. 
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
            turn_around()   # Now back to (1, 1), facing east.
            put_checkerboard_and_back()  # Now back to (1, 1), facing east. 1st Street's filled in checkerboard pattern.
            while front_is_clear():
                triangles()


def put_checkerboard_and_back():
    """
    Pre-condition: Karel's at (1, 1), facing east. There's no beeper on 1st Street.
    Post-condition: Karel's at (1, 1), facing east. 1st Street's filled in checkerboard pattern.
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def triangles():
    """
    A triangle has three vertices, left, top and right vertices.
    Pre-condition: Karel is on a beeper (left vertex).
    Post-condition: The left beeper is picked up and the top beeper is put. Karel's on the beeper where a right vertex
    is supposed to be.
    Exceptions when Karel has to go up to the next street:
    1. When Karel makes one move to the right, there's the wall.
    2. When there's no more beeper on the right as a right vertex.
    3. When Karel's on the right vertex and there's the wall.
    """
    pick_beeper()
    move()
    if front_is_clear():
        move()
        if on_beeper():
            turn_around()
            move()
            turn_right()
            move()
            put_beeper()
            turn_around()
            move()
            turn_left()
            move()
            if not front_is_clear():  # Exception 3
                pick_beeper()
                go_next_street()
        else:  # Exception 2
            go_next_street()
    else:  # Exception 1
        go_next_street()


def go_next_street():
    """
    Pre-condition: (Corresponding to Exceptions 1-3 of the triangles() function)
    1. Karel meets the right wall, facing east.
    2. Karel is not on beeper, facing east.
    3. Karel meets the right wall, facing east and he's on beeper.
    Post-condition: Karel is on a left vertex, facing east.
    There is one exception when Karel reaches the top point of the pyramid, and that's when we can mark the midpoint.
    """
    turn_around()  # Face west
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()  # Face east
    while not on_beeper():  # Go east until a beeper is stepped on
        move()
    move()
    if front_is_clear():
        move()
        if on_beeper():  # Found the right vertex
            turn_around()
            for i in range(2):  # Go back to the left vertex
                move()
            turn_around()  # Face east
        else:  # Exception: Right vertex is not found, which means it's already the top point of the pyramid.
            mark_midpoint()
    elif not front_is_clear():  # Exception: Right vertex is not found,
        # which means it's already the top point of the pyramid.
        mark_midpoint()


def mark_midpoint():
    """
    Pre-condition: Karel is not on beeper, facing east.
    Post-condition: Karel is on the midpoint. The midpoint beeper is put on 1st Street.
    """
    # Right vertex is not found, which means it's already the top point of the pyramid.
    if front_is_clear():
        turn_around()  # Face west
        for i in range(2):  # Go back to the top point
            move()
    elif not front_is_clear():
        turn_around()
        while not on_beeper():
            move()
    pick_beeper()
    turn_left()  # Face south
    while front_is_clear():
        move()
    put_beeper()  # Midpoint on 1st Street


def turn_around():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
