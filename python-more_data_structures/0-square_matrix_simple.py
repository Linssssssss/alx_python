def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = [[0 for _ in row] for row in matrix]

    # Iterate over the rows and columns of the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Square each element and store it in the corresponding position of the new matrix
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
