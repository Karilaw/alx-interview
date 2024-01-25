#!/usr/bin/python3
"""
This script reads from stdin, parses logs in a specific format
"""

import sys
import signal


# Initialize variables
status_codes = {str(i): 0 for i in [200, 301, 400, 401, 403, 404, 405, 500]}
total_size = 0
line_count = 0


def print_stats():
    """
    Prints the total file size and the number of lines by status code.
    Status codes are printed in ascending order.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """
    Handles keyboard interruption (CTRL + C).
    Prints the statistics and exits the program.
    """
    print_stats()
    sys.exit(0)


# Handle Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            size = int(parts[-1])
            status_code = parts[-2]

            if status_code in status_codes:
                status_codes[status_code] += 1

            total_size += size
            line_count += 1

            if line_count % 10 == 0:
                print_stats()

        except ValueError:
            continue

except KeyboardInterrupt:
    pass

finally:
    print_stats()
