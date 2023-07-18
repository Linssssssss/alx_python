#!usr/bin/python3
import random
number = random.randint(-10, 10)
print(number)
if number > 0:
    print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
        else:
            print("The number is zero.")