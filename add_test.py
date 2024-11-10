import unittest
from AddNumbers import Calculator

class TestAdd(unittest.TestCase):
    def test_add(self):
        result = Calculator.add(3, 7)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
