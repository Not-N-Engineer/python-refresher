import unittest
import hello
import numpy as np
import pytest


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
    
    def test_add(self):
        assert hello.add(5, 3) == 8          # Test for positive numbers
        assert hello.add(-2, 2) == 0         # Test for negative and positive number
        assert hello.add(0, 0) == 0          # Test for zero addition

    def test_sub(self):
        assert hello.sub(5, 3) == 2     # Test for positive numbers
        assert hello.sub(-2, -2) == 0    # Test for negative numbers
        assert hello.sub(0, 5) == -5    # Test for zero minuend

    def test_mul(self):
        assert hello.mul(5, 3) == 15    # Test for positive numbers
        assert hello.mul(-2, 2) == -4   # Test for negative and positive number
        assert hello.mul(0, 100) == 0   # Test for multiplication by zero

    def test_div(self):
        assert hello.div(-4, 2) == -2     # Test for negative and positive number
        assert hello.div(5, 2) == 2.5     # Test for division resulting in float
        with pytest.raises(ValueError, match="Can't divide by zero!"):
            hello.div(5, 0)               # Test division by zero

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)
        self.assertEqual(hello.sin(np.pi/2), 1)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)
        self.assertEqual(hello.cos((np.pi)/2), np.cos((np.pi)/2))

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)
        self.assertEqual(hello.tan(np.pi), np.tan(np.pi))

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)
        self.assertEqual(hello.cot((np.pi)/2), 1/np.tan((np.pi)/2))


if __name__ == "__main__":
    unittest.main()
