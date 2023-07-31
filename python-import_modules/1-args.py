import sys

# Retrieve the number of arguments passed to the script
num_args = len(sys.argv) - 1

# Print the number of arguments
print("Number of argument{}: {}".format('s' if num_args != 1 else '', num_args), end='')

# Print whether it's "argument" or "arguments" and add a new line
print(" argument{}:".format('' if num_args == 1 else 's'))

# Print each argument with its position
for i, arg in enumerate(sys.argv[1:], 1):
    print("{}: {}".format(i, arg))
