def raise_exception():
    try:
        value = "Hello" + 5
    except TypeError:
        print("Type error occured!")
        raise 

raise_exception()