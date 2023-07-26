def print_matrix_integer(matrix=[[]]):
    # Get the number of rows and columns in the matrix
    for row in matrix:
        for col_idx, col in enumerate(row):
            # Print each integer in the matrix with proper formatting
            print("{:d}".format(col), end=" ")
            if col_idx < len(row) - 1:
                print(" ", end="")
            print() #Move to the next line after each row
