def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string
# Test the function      
input_string = " Holberton School Chicago is fun."
result = no_c(input_string)
print(result)
