from program import validate_input, process_number

def test_valid_number_input():

#checks if the string is converted correctly

    assert process_number("42") == 42

def test_invalid_number_input():

#checks that invalid number returns none

    assert process_number("abc") is None