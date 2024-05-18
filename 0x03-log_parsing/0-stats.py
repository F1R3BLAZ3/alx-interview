#!/usr/bin/python3
"""
Log Statistics

This script reads log lines from standard input and computes statistics such as total file size and the count of various HTTP status codes.
Statistics are printed after every 10 lines and upon termination via keyboard interrupt (CTRL + C).
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
    global total_size, status_code_counts
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
        parts = line.split()
        if len(parts) != 10:
            continue
        
        ip, dash, date, request, status_code, file_size = parts[0], parts[1], parts[2], parts[3:6], parts[6], parts[9]
        
        # Validate the request format
        if request[0] != '"GET' or request[2] != 'HTTP/1.1"':
            continue

        try:
            file_size = int(file_size)
            total_size += file_size
        except ValueError:
            continue

        # Update status code count if valid
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        
        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)

# Print statistics for any remaining lines if end of file is reached
print_statistics()
