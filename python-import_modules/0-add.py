# Assign values to variables a and b
a = 1
b = 2

# Define the add function
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

# Calculate the result using the add function
result = add(a, b)

# Print the result using string formatting
print(f"{a} + {b} = {result}")
