
# now lets look at functions
def test_number(the_number):
    # comparing numbers
    if the_number > 3:
        print(f"{the_number} is bigger than 3")
    else:
        print(f"{the_number} is smaller or equal to 3")

    if the_number == 3:
        print(f"{the_number} is equal to 3")
    elif the_number >= 3:
        print(f"{the_number} is equal to or bigger than 3")
    else:
        print(f"{the_number} is smaller than 3")


def test_string(the_string):
    # this is a if statement, its a test
    if the_string == 'Hello World':
        print(f"{the_string} is saying hello to the world")

    if 'Hello' in the_string:
        print(f"{the_string} is saying hello")


def test_float(the_float):
    # comparing floats
    if the_float > 3:
        print(f"{the_float} is bigger than or equal to 3")
    else:
        print(f"{the_float} is smaller than 3")

    if the_float >= 3:
        print(f"{the_float} is equal to or bigger than 3")
    else:
        print(f"{the_float} is smaller than 3")

    if the_float >= 3.3:
        print(f"{the_float} is equal to or bigger than 3.3")
    else:
        print(f"{the_float} is smaller than 3.3")


im_a_string = 'Hello World'
im_a_number = 3
im_a_float = 3.3
im_a_boolean = True

test_string(im_a_string)
test_number(im_a_number)
test_float(im_a_float)
