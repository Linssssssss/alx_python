import sys

# Retrieve the number of arguments passed to the script
num_args = len(sys.argv) - 1

# Check if any arguments were passed and print the appropriate output
print(f"Number of argument{'s' if num_args != 1 else ''}: {num_args}{'.' if num_args == 0 else ':'}")

for i in range(1, num_args + 1):
    print(f"{i}: {sys.argv[i]}")
