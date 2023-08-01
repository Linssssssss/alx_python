#!/usr/bin/env python3

# Initialize an empty string to store the output
output = ""

# Loop through numbers from 0 to 98 (inclusive)
for num in range(99):
    # Append the number in decimal and hexadecimal format to the output string
    output += f"{num} = 0x{num:x}\n"

# Print the output string
print(output, end="")
