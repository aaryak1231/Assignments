def validate_input(user_input):
    """Validates that input is not empty and returns True/False"""
    if user_input and len(user_input) > 0:
        return True
    return False

def process_number(num_string):
    """Converts string to number if valid"""
    try:
        return int(num_string)
    except ValueError:
        return None