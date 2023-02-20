"""
File: StoneMasonKarel.py
Name: Jane
--------------------------------
This program shows Karel starting at the left side wall of the house at Street 1, Avenue 1, in short: (1, 1)
building or fixing a column, which is 5 beepers tall
in each avenue that is either on the right or left side of the arch,
and that the distances between each side of arches being always 3 avenues away,
and that Karel ending up at the right side wall of the house, at the last avenue, Street 1, facing east.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel is at (1, 1) facing east. There might be some columns to be built or fixed, in short: filled.
    Post-condition: All the columns are filled. Karel is at (1, last avenue) facing east.
    """
    """
    Any house must have at least one arch (that is to say, two columns). 
    So first we let Karel go upward building the first column on Avenue 1. And now he's at (5, 1). 
    And then we let him move right to Avenue 5 where the second column is supposed to be. Now at (5, 5).
    """
    fill_column_upward()  # 1st column
    for i in range(4):  # Go right
        move()
    """
    Now Karel's at the top of the second column, we'll use the following while loop 
    to let Karel go down, right and up. (Let's call it the "U" shape)  
    It is worth noting that, if the house has only two columns, the following loop will be skipped.
    """
    while front_is_clear():
        fill_column_downward()
        for i in range(4):
            move()
        fill_column_upward()
        if front_is_clear():
            """
            At this point we have to check if Karel reaches the right side wall. 
            If he doesn't reach the wall (front clear), he can go right. 
            And now this is the end of this while loop. 
            We can go to the beginning of the loop again since front is clear.
            If he reaches the wall (front not clear), he can't go right.
            And now this is the end of this while loop. 
            We can't go to the beginning of the loop anymore since front is not clear.
            """
            for i in range(4):  # Go right
                move()
    """
    When we leave the while loop above (or skipped, if the house has only two columns), 
    it means Karel's at the last column and he's on Street 5. We let him go downward and fill the column.
    """
    fill_column_downward()


def fill_column_upward():
    """
    Pre-condition: Karel is on Street 1, facing east. The column on the avenue where Karel is on might need to be filled.
    Post-condition: Karel is on Street 5, same avenue, facing east. The column is filled.
    """
    turn_left()
    if not on_beeper():
        put_beeper()
    for i in range(4):
        move()
        if not on_beeper():
            put_beeper()
    turn_right()


def fill_column_downward():
    """
    Pre-condition: Karel is on Street 5, The column on the avenue where Karel is on might need to be filled.
    Post-condition: Karel is on Street 1, same avenue, facing east. The column is filled.
    """
    turn_right()
    if not on_beeper():
        put_beeper()
    for i in range(4):
        move()
        if not on_beeper():
            put_beeper()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
