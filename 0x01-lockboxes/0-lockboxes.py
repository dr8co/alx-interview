#!/bin/python3
"""
Module for lockboxes method.
"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened.
    """
    if len(boxes) == 0:
        return False
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    if len(keys) == len(boxes):
        return True
    return False
