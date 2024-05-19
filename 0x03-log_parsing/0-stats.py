#!/usr/bin/python3
"""
Log parsing script.

This script reads log lines from standard input and computes statistics such as
total file size and the count of various HTTP status codes.
Statistics are printed after every 10 lines and upon termination via keyboard
interrupt (CTRL + C).
"""

import sys
import signal

# Initialize variables
total_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_statistics():
    """
    Prints the accumulated statistics.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


def handle_interrupt(signal, frame):
    """
    Handles keyboard interrupt (CTRL + C) to print statistics.
    """
    print_statistics()
    sys.exit(0)


# Register the interrupt signal handler
signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Process status code
        try:
            status_code = parts[-2]
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
        except IndexError:
            continue

        # Process file size
        try:
            file_size = int(parts[-1])
            total_size += file_size
        except (IndexError, ValueError):
            continue

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    raise

# Print statistics for any remaining lines if end of file is reached
print_statistics()
