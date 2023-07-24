import sys
def print_arguments():
    num_args = len(sys.argv) - 1
    print(f"Number of argument(s): {num_args}", end=" ")

    if num_args == 1:
        print("argument:", end=" ")
    else:
        print("arguments:", end=" ")
    if num_args > 0:
        print()
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"{i}: {arg}")
    else:
        print(".")
print_arguments()