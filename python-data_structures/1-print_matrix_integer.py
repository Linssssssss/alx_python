def print_matrix_integer(matrix=[[]]):
    # Get the dimensions of the matrix
    rows = len(matrix)
    if rows == 0:
        return

    columns = len(matrix[0])

    # Calculate the maximum width of each element for formatting purposes
    max_width = max(len(str(matrix[i][j])) for i in range(rows) for j in range(columns))

    # Print the matrix
    for row in matrix:
        for i in range(columns):
            print("{:>{width}}".format(row[i], width=max_width), end=" ")
        print()