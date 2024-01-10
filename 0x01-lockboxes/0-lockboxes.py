#!/usr/bin/python3
""" 0x01. Lockboxes """


def canUnlockAll(boxes):
    """ Create a set to store the keys
    """
    keys = {0}
    while True:
        new_keys = set()
        for key in keys:
            for box in boxes[key]:
                if box < len(boxes):
                    new_keys.add(box)
        if not new_keys - keys:
            break
        keys.update(new_keys)

    return len(keys) == len(boxes)
