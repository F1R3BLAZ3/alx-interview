#!/usr/bin/python3
"""
Log Processor

This script processes log data from stdin, specifically focusing on lines
related to GET requests for /projects/260 in HTTP/1.1 format.  It calculates
and prints total file size and counts of various HTTP status codes.

Usage:
    python3 script.py < access.log
"""

import sys


def output(total_size, status_code_counts):
    """
    Helper function to display stats.

    Parameters:
        total_size (int): Total file size.
        status_code_counts (dict): Counts of different HTTP status codes.
    """
    print(f'Total file size: {total_size}')
    for code in sorted(status_code_counts):
        if status_code_counts[code]:
            print(f'{code}: {status_code_counts[code]}')


if __name__ == "__main__":
    # Initialize variables
    total_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0,
                          401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        # Process stdin line by line
        for line in sys.stdin:
            # Parse line format
            parts = line.split()
            if len(parts) != 12 or \
                    parts[5] != "\"GET" or \
                    parts[6] != "/projects/260" or \
                    parts[8] != "HTTP/1.1":
                continue

            # Extract relevant information
            status_code = int(parts[9])
            file_size = int(parts[10])

            # Update metrics
            total_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                output(total_size, status_code_counts)

    except KeyboardInterrupt:
        # Handle keyboard interruption
        output(total_size, status_code_counts)
        sys.exit(0)
