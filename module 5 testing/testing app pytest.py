from program import validate_input, process_number

def test_valid_number_input():
    """Test that valid number string is converted correctly"""
    assert process_number("42") == 42

def test_invalid_number_input():
    """Test that invalid number string returns None"""
    assert process_number("abc") is None