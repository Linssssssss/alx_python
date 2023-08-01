for i in range(10):
    for j in range(i + 1, 10):
        # Check if it's the last combination
        if i == 8 and j == 9:
            # If it's the last combination, print without comma and space
            print("{:d}{:d}".format(i, j))
        else:
            # For other combinations, print with comma and space
            print("{:d}{:d}, ".format(i, j), end="")
