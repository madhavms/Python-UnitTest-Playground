import unittest
import calc

class TestCalc(unittest.TestCase):
    """Test for addition"""
    def test_add(self):
        for i in range(10000):
            result = calc.add(10, i)
            self.assertEqual(result, 10 + i)
    """Test for subtract"""
    def test_subtract(self):
        for i in range(10000):
            result = calc.subtract(10, i)
            self.assertEqual(result, 10 - i)
    """Test for multiply"""
    def test_multiply(self):
        for i in range(10000):
            result = calc.multiply(10, i)
            self.assertEqual(result, 10 * i)
    """Test for divide"""
    def test_divide(self):
        for i in range(10000):
            if i == 0:
                with self.assertRaises(ValueError):
                    calc.divide(10, i)
            else:
                result = calc.divide(10, i)
                self.assertEqual(result, 10 / i)

if __name__ == '__main__':
    unittest.main()
