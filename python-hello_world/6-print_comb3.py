#!/usr/bin/env python3

# Loop through the tens digit from 0 to 8
for tens in range(9):
    # Loop through the ones digit from tens + 1 to 9
    for ones in range(tens + 1, 10):
        # Print the two-digit combination
        print(f"{tens}{ones}", end=", " if tens < 8 else "\n")
