for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        print("{:02d}".format(first_digit), "{:02d}".format(second_digit), end="")
        if first_digit != 8 or second_digit != 9:
            print(",", end="")
        else:
            print()