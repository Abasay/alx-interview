#!/usr/bin/python3
"""Module for validUtf8 method"""


def validUTF8(data):
    """Determines if given data represents valid UTF-8 encoding
    Args:
        data: list of integers
    Returns:
        True if valid UTF-8 encoding, otherwise False
    """
    # Number of bytes in the current UTF-8 character
    curr_bytes = 0

    # Mask to check if the most significant bit(msbs) is set or not
    mask_1 = 1 << 7

    # Mask to check if the second most significant bit(msbs) is set or not
    mask_2 = 1 << 6
    for num in data:

        # Get the number of set most significant bits in the byte if
        # this is the starting byte of an UTF-8 character.
        mask_0 = 1 << 7
        if curr_bytes == 0:
            while mask_0 & num:
                curr_bytes += 1
                mask_0 = mask_0 >> 1

            # 1 byte characters
            if curr_bytes == 0:
                continue

            # Invalid scenarios according to the rules of the problem.
            if curr_bytes == 1 or curr_bytes > 4:
                return False
        else:
            # If this byte is a part of an existing UTF-8 character, then we
            # simply have to look at the two most significant bits and we make
            # use of the masks we defined before.
            if not (num & mask_1 and not (num & mask_2)):
                return False
        curr_bytes -= 1
    return curr_bytes == 0
