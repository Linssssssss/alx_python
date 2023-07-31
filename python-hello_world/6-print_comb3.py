for tens_digit in range(10):
    for units_digit in range(tens_digit + 1, 10):
        print(f"{tens_digit}{units_digit}", end=", " if tens_digit != 8 or units_digit != 9 else "\n")
