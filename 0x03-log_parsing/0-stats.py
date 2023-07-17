#!/usr/bin/python3
"""
Module for log parsing method.
"""


import sys


def print_stats(file_size, status_codes):
    """
    Method to print log parsing stats.
    """
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    counter = 0
    try:
        for line in sys.stdin:
            if counter != 0 and counter % 10 == 0:
                print_stats(file_size, status_codes)
            counter += 1
            parsed_line = line.split()
            try:
                file_size += int(parsed_line[-1])
            except Exception:
                pass
            try:
                status_codes[parsed_line[-2]] += 1
            except Exception:
                pass
        print_stats(file_size, status_codes)
    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise
