def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError as e:
        print(f"Name error occurred: {e}")

raise_exception_msg("This is a custom name exception.")
    