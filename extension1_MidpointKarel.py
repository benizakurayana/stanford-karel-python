"""
File: extension1_MidpointKarel.py
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
    Geometrically, the midpoint of a side of a square is perpendicular to the intersection of the square's diagonals.
    This is our core idea of this algorithm.
    In Type 1, there won't be a intersection when we draw diagonals with beepers. 
    However, there will be four adjacent beepers in the center. We can use this to mark the midpoint.
    As for Type 2, there will be two beepers on the intersection, when we draw diagonals with beepers. 
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
            put_forward_slash()
            turn_around()
            while front_is_clear():
                move()
            turn_right()  # Now at bottom right corner of the square, facing west.
            put_back_slash()
            turn_around()  # Now at top left corner, facing south
            pick_and_check()  # Now either at top right corner facing north, or at bottom right corner facing south.
            turn_around()
            mark_midpoint()


def put_forward_slash():
    """
    Pre-condition: Karel's at (1, 1). There's no beeper.
    Post-condition: Karel's at top right corner of the square. There are beepers on (1, 1), (2, 2), (3, 3), and so on,
    all the way to the top right corner, which forms a diagonal of the square from bottom left to top right.
    """
    put_beeper()
    while front_is_clear():

        move()
        if front_is_clear():
            turn_left()
            move()
            put_beeper()
            turn_right()
        else:
            if facing_east():
                turn_left()
                move()
                put_beeper()


def put_back_slash():
    """
    Pre-condition: Karel's at bottom right corner of the square.
    Post-condition: Karel's at top left corner of the square. There are beepers on the diagonal of the square
    from bottom right to top left.
    """
    put_beeper()
    while front_is_clear():

        move()
        if front_is_clear():
            turn_right()
            move()
            put_beeper()
            turn_left()
        else:
            if facing_west():
                turn_right()
                move()
                put_beeper()


def pick_and_check():
    """
    Pre-condition: Karel's at top left corner of the square.
    Post-condition: Karel goes upward and downward, picking up the beepers and meanwhile checking
    if there are two beepers that are adjacent. Once found, pick all the remaining beepers.
    """
    """
    It is worth noting that, in the case of a Type 2 board (which is with odd number of corners), 
    No adjacent beepers will be found. However, Karel picks up only one beeper when he checks through the board. 
    There will be still one beeper on the intersection.  
    """
    while front_is_clear():
        if on_beeper():
            move()
            if on_beeper():  # If Karel finds two beepers that are adjacent.
                pick_beeper()  # The second adjacent beeper is picked while the first one remains.
                clear_the_rest()

            else:  # If there is no adjacent beeper
                turn_around()
                move()
                pick_beeper()  # Now Karel goes back to pick up the beeper and continue to go forward.
                turn_around()
                move()
        else:  # If Karel is not on beeper.
            move()
        if not front_is_clear():
            """
            When Karel makes one move, we have to check if he meets the bottom or top side 
            of the square and let him go to the next avenue.
            """
            if on_beeper():
                pick_beeper()
            if facing_south():
                if left_is_clear():
                    """ 
                    If Karel's front is not clear and that he's facing south, and that his left is clear,
                    it means he's at the bottom side of the square and there are more avenues to go 
                    on the east direction. Then, he shall make a U turn to the next avenue.
                    """
                    turn_left()
                    move()
                    turn_left()
            else:
                if right_is_clear():
                    """ 
                    If Karel's front is not clear and that he's facing north, and that his right is clear,
                    it means he's at the top side of the square and there are more avenues to go 
                    on the east direction. Then, he shall make a U turn to the next avenue.
                    """
                    turn_right()
                    move()
                    turn_right()


def clear_the_rest():
    """
    Pre-condition: Karel finds two beepers that are adjacent.
    Post-condition: The remaining beepers are all picked up. Only the first one of the adjacent beepers left.
    """
    while front_is_clear():
        move()
        if on_beeper():
            pick_beeper()
        if not front_is_clear():
            """
            When Karel makes one move, we have to check if he meets the bottom or top side 
            of the square and let him go to the next avenue.
            """
            if on_beeper():
                pick_beeper()
            if facing_south():
                if left_is_clear():
                    turn_left()
                    move()
                    turn_left()
                if on_beeper():
                    pick_beeper()
            else:
                if right_is_clear():
                    turn_right()
                    move()
                    turn_right()
                if on_beeper():
                    pick_beeper()


def mark_midpoint():
    """
    Pre-condition: Either at top right corner facing south, or at bottom right corner facing north.
    Post-condition: The midpoint beeper is put on 1st Street.
    """
    while front_is_clear():
        if on_beeper():  # When Karel finds the only beeper left.
            pick_beeper()
            if facing_north():
                turn_around()
            while front_is_clear():
                move()
            put_beeper()  # Put the beeper on 1st Street.

        else:
            move()
        if not front_is_clear() and not on_beeper():
            """
            When Karel makes one move, we have to check if he meets the bottom or top side 
            of the square and let him go to the next avenue.
            """
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


def turn_around():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
