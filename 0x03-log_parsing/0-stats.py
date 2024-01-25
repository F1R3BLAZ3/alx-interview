#!/usr/bin/python3
import sys

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
            print(f'Total file size: {total_size}')
            for code in sorted(status_code_counts):
                if status_code_counts[code] > 0:
                    print(f'{code}: {status_code_counts[code]}')

except KeyboardInterrupt:
    # Handle keyboard interruption
    print(f'Total file size: {total_size}')
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f'{code}: {status_code_counts[code]}')
    sys.exit(0)
