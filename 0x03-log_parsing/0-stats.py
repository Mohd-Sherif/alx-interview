#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""
import sys
import signal


# Initialize global variables
total_file_size = 0
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def print_stats():
    """Prints the collected statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

def handle_interrupt(signal, frame):
    """Handles keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Setup signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)

# Process input line by line
try:
    for line in sys.stdin:
        # Parse the line to match the expected format
        parts = line.split()
        if len(parts) != 7:
            continue  # Skip lines that don't match the expected format
        
        try:
            # Extract relevant fields
            ip_address = parts[0]
            date = parts[2] + ' ' + parts[3]
            method = parts[4]
            status_code = int(parts[5])
            file_size = int(parts[6])

            # Ensure the line matches the expected format
            if method != '"GET':
                continue

            # Update total file size
            total_file_size += file_size

            # Update status code count
            if status_code in status_code_count:
                status_code_count[status_code] += 1

            line_count += 1

            # Every 10 lines, print the statistics
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            continue  # Skip any lines with improper format or missing data

except KeyboardInterrupt:
    # Handle CTRL + C before signal catches
    print_stats()
    sys.exit(0)
