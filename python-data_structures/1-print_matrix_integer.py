def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Use str.format() to priny integers without casting them into strings
            print("{:d}".format(row[i]), end="")
            if i != len(row) - 1:
                print(" ", end="")
            print()