#!/usr/bin/python3
"""
Module to check the validity of UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if the given list of bytes represents a valid UTF-8 encoding.

    Parameters:
    - data (list): A list of integers representing bytes.

    Returns:
    - bool: True if the data represents a valid UTF-8 encoding, False otherwise
    """
    # Count of remaining bytes for a UTF-8 character
    remaining_bytes = 0

    for byte in data:
        # If no remaining bytes from previous character
        if remaining_bytes == 0:
            # Check the number of leading ones to
            # determine the length of the UTF-8 character
            if byte >> 7 == 0b0:
                continue  # 1-byte character
            elif byte >> 5 == 0b110:
                remaining_bytes = 1  # 2-byte character
            elif byte >> 4 == 0b1110:
                remaining_bytes = 2  # 3-byte character
            elif byte >> 3 == 0b11110:
                remaining_bytes = 3  # 4-byte character
            else:
                return False  # Invalid leading byte pattern
        else:
            # Check if the current byte is a continuation byte
            # (starts with 0b10)
            if byte >> 6 != 0b10:
                return False  # Invalid continuation byte
            remaining_bytes -= 1

    # If all bytes have been processed and no incomplete character
    return remaining_bytes == 0
