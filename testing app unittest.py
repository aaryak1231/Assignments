import unittest
from program import validate_input, process_number

class TestInput(unittest.TestCase):
    def test_valid_input(self):

#checks if valid input returns true

        self.assertTrue(validate_input("hello"))
    
    def test_empty_input(self):

#checks if empty inpput returns false

        self.assertFalse(validate_input(""))

if __name__ == '__main__':
    unittest.main()