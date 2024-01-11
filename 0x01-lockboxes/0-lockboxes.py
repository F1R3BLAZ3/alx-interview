#!/usr/bin/python3
"""
    Determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each inner list represents a box
                      and contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True  # The first box is initially unlocked

    keys_stack = [0]  # Start with the keys from the first box

    while keys_stack:
        current_box = keys_stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                keys_stack.append(key)

    return all(unlocked_boxes)
