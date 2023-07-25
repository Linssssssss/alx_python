def print_matrix_integer(matrix=[[]]):
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    for i in range(num_rows):
        for j in range(num_rows):
            print("{:d}".format(matrix[i][j]), end="")
            if j < num_cols - 1:
                print(" ", end="")
                print()
# Test the function
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)