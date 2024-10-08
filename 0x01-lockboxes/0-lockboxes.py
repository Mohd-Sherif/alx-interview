#!/usr/bin/python3

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


boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
