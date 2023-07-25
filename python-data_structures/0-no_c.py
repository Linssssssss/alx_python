def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string
        
input_string = " Cats and dogs are cute."
result = no_c(input_string)
print(result)