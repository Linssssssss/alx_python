#!/usr/bin/env python3
import random

# Assign a random signed number to the variable 'number'
number = random.randint(-10000, 10000)

# Get the last digit of the number (taking into account negative numbers)
last_digit = abs(number) % 10
if number < 0:
    last_digit *= -1

# Print the result based on the last digit
print(f"Last digit of {number} is {last_digit}", end=' ')

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
