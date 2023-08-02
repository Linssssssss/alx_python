def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci_numbers = [0, 1]

    for i in range(2, n):
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)

    return fibonacci_numbers[:n]
