def pow(a, b):
    result = 1
    if b < 0:
        a = 1 / a
        b = -b
    for _ in range(b):
        result *= a
    return round(result, 2)  # Round the result to 2 decimal places
