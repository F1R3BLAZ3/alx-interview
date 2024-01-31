def validUTF8(data):
    """Check if the given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers representing 1 byte of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """
    # Helper function to check if the current byte is a valid continuation byte
    def is_continuation(byte):
        return 0b10000000 <= byte <= 0b10111111

    # Iterate through the data bytes
    i = 0
    while i < len(data):
        # Get the number of bytes for the current character
        num_bytes = 0
        mask = 0b10000000
        while data[i] & mask:
            num_bytes += 1
            mask >>= 1

        # Check if the number of bytes is within the valid range (1 to 4 bytes)
        if num_bytes < 1 or num_bytes > 4:
            return False

        # Check if the following bytes are valid continuation bytes
        for j in range(1, num_bytes):
            i += 1
            if i >= len(data) or not is_continuation(data[i]):
                return False

        i += 1  # Move to the next character

    return True
