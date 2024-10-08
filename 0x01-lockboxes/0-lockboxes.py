#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.
    - Prototype: def canUnlockAll(boxes)
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
        - There can be keys that do not have boxes
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    # A set to track which boxes can be opened
    opened_boxes = set()

    # Start with the first box which is initially unlocked
    opened_boxes.add(0)

    # A stack to hold the boxes we can explore
    stack = [0]

    # Continue exploring until there are no more boxes to explore
    while stack:
        current_box = stack.pop()

        # Iterate over the keys found in the current box
        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                # Add the newly opened box to the stack for exploration
                stack.append(key)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
