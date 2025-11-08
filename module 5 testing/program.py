def validate_input(user_input): 

#this function checks if user input is valid. If returns true length of the input is more than 0 so not empty, if not false.

    if user_input and len(user_input) > 0:
        return True
    return False

def process_number(num_string):

#this converts string to number if it is valid

    try:
        return int(num_string)
    except ValueError:
        return None