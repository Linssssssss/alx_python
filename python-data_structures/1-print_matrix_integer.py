def print_matrix_integer(matrix=[[]]):
    # Get the number of rows and columns in the matrix
    for row in matrix:
        for col in row:
            # Print each integer in the matrix with proper formatting
            print("{:d}".format(col), end=" " if col != row[-1] else "")
            print() #Move to the next line after each row
            