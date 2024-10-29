#!/usr/bin/python3
"""
A method that determines if a given data set represents
a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    validUTF8 Method
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits of each byte
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    for byte in data:
        # Only consider the last 8 bits of the byte
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):  # 1-byte character has a leading 0
                return False
        else:
            # Check that the byte is a continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
