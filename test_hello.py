import unittest
import hello
import numpy as np


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
    
    def test_add(self):
        self.assertEqual(hello.add(5, 3), 8)          # Test for positive numbers
        self.assertEqual(hello.add(-2, 2), 0)         # Test for negative and positive number
        self.assertEqual(hello.add(2, -2), 0)         # Test for negative and positive number
        self.assertEqual(hello.add(3.564, 5.132), 8.696)
        self.assertEqual(hello.add(0, 0), 0)          # Test for zero addition

        self.assertNotEqual(hello.add(3.564, 5.132), 9)
        with self.assertRaises(TypeError):
            hello.add("hi", 3)
        with self.assertRaises(TypeError):
            hello.add('c', 3)
        with self.assertRaises(TypeError):
            hello.add([3], 3)

    def test_sub(self):
        self.assertEqual(hello.sub(5, 3), 2)     # Test for positive numbers
        self.assertEqual(hello.sub(-2, 2), -4)   # Test for negative and positive number
        self.assertEqual(hello.sub(2, -2), 4)    # Test for negative and positive number
        self.assertEqual(hello.sub(-2, -2), 0)   # Test for negative numbers
        self.assertEqual(hello.sub(0, 5), -5)    # Test for zero minuend
        self.assertAlmostEqual(hello.sub(3.564, 5.132), -1.568, 3)
        self.assertEqual(hello.sub(0, 0), 0)          

        self.assertNotEqual(hello.sub(3.564, 5.132), -1)
        with self.assertRaises(TypeError):
            hello.sub("hi", 3)
        with self.assertRaises(TypeError):
            hello.sub("hi", "world")
        with self.assertRaises(TypeError):
            hello.sub('c', 3)
        with self.assertRaises(TypeError):
            hello.sub([3], 3)

    def test_mul(self):
        self.assertEqual(hello.mul(5, 3), 15)    # Test for positive numbers
        self.assertEqual(hello.mul(-2, 2), -4)   # Test for negative and positive number
        self.assertEqual(hello.mul(2, -2), -4)   # Test for negative and positive number
        self.assertEqual(hello.mul(-2, -2), 4)   # Test for negative numbers
        self.assertEqual(hello.mul(0, 100), 0)   # Test for multiplication by zero
        self.assertEqual(hello.mul(0, 0), 0)    
        self.assertAlmostEqual(hello.mul(3.564, 5.132), 18.290448, 6)
        self.assertEqual(hello.mul(3.5, 5), 17.5)          

        self.assertNotEqual(hello.mul(3.564, 5.132), 9)
        with self.assertRaises(TypeError):
            hello.mul("hi", "world")

    def test_div(self):
        self.assertEqual(hello.div(4, 2), 2)
        self.assertEqual(hello.div(5, 5), 1)
        self.assertEqual(hello.div(-4, 2), -2)     # Test for negative and positive number
        self.assertEqual(hello.div(4, -2), -2)     # Test for negative and positive number
        self.assertEqual(hello.div(-4, -2), 2)     # Test for negative numbers
        self.assertEqual(hello.div(5, 2), 2.5)     # Test for division resulting in float
        self.assertAlmostEqual(hello.div(5, 2.3), 2.173913043478261, 5)
        self.assertAlmostEqual(hello.div(5.0, 2.3), 2.173913043478261, 5)

        with self.assertRaises(ValueError):
            hello.div(5, 0)                        # Test division by zero
        with self.assertRaises(TypeError):
            hello.div("hi", 3)
        with self.assertRaises(TypeError):
            hello.div("hi", "world")
        with self.assertRaises(TypeError):
            hello.div('c', 3)
        with self.assertRaises(TypeError):
            hello.div([3], 3)

    def test_sqrt(self):
        self.assertAlmostEqual(hello.sqrt(2), 1.41421356, 5)
        self.assertAlmostEqual(hello.sqrt(520.3), 22.81008548, 5)
        self.assertEqual(hello.sqrt(0), 0)

        with self.assertRaises(TypeError):
            hello.sqrt("hi")
        with self.assertRaises(TypeError):
            hello.sqrt('c')
    
    def test_power(self):
        self.assertEqual(hello.power(2, 2), 4)
        self.assertAlmostEqual(hello.power(2, 2.5), 5.65685424, 5)
        self.assertEqual(hello.power(2.5, 2), 6.25)
    
    def test_log(self):
        self.assertAlmostEqual(hello.log(2), 0.69314718, 5)
        self.assertAlmostEqual(hello.log(2.5), 0.91629073, 5)
        self.assertAlmostEqual(hello.log(2123), 7.66058546, 5)

        with self.assertRaises(TypeError):
            hello.log("hi")
        with self.assertRaises(TypeError):
            hello.log('c')
    
    def test_exp(self):
        self.assertAlmostEqual(hello.exp(2), 7.38905609, 5)
        self.assertAlmostEqual(hello.exp(2.5), 12.18249396)
        self.assertEqual(hello.exp(np.log(2)), 2)

        with self.assertRaises(TypeError):
            hello.exp("hi")
        with self.assertRaises(TypeError):
            hello.exp('c')

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertAlmostEqual(hello.sin(1), 0.8414709848078965, 5)
        self.assertEqual(hello.sin(np.pi/2), 1)

        for i in range(3):
            self.assertLess(hello.sin(0            + i*np.pi), 0.000000000000001)
            self.assertGreater(hello.sin(0         + i*np.pi), -0.000000000000001)
            self.assertLess(hello.sin(0            - i*np.pi), 0.000000000000001)
            self.assertGreater(hello.sin(0         - i*np.pi), -0.000000000000001)
            
            self.assertEqual(hello.sin(((np.pi)/2) + i*2*np.pi), 1)
            self.assertEqual(hello.sin(((np.pi)/2) - i*2*np.pi), 1)
            self.assertEqual(hello.sin(((3*np.pi)/2) + i*2*np.pi), -1)
            self.assertEqual(hello.sin(((3*np.pi)/2) - i*2*np.pi), -1)

        with self.assertRaises(TypeError):
            hello.sin("hi")
        with self.assertRaises(TypeError):
            hello.sin('c')

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertAlmostEqual(hello.cos(1), 0.5403023058681398, 5)
        self.assertLess(hello.cos((np.pi)/2), 0.000000000000001)
        self.assertGreater(hello.cos((np.pi)/2), -0.000000000000001)
        
        for i in range(3):
            self.assertLess(hello.cos(((np.pi)/2)    + i*np.pi), 0.000000000000001)
            self.assertGreater(hello.cos(((np.pi)/2) + i*np.pi), -0.000000000000001)
            self.assertLess(hello.cos(((np.pi)/2)    - i*np.pi), 0.000000000000001)
            self.assertGreater(hello.cos(((np.pi)/2) - i*np.pi), -0.000000000000001)
            
            self.assertEqual(hello.cos(0             + i*2*np.pi), 1)
            self.assertEqual(hello.cos(0             - i*2*np.pi), 1)
            self.assertEqual(hello.cos(np.pi         + i*2*np.pi), -1)
            self.assertEqual(hello.cos(np.pi         - i*2*np.pi), -1)

        with self.assertRaises(TypeError):
            hello.cos("hi")
        with self.assertRaises(TypeError):
            hello.cos('c')

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertAlmostEqual(hello.tan(1), 1.5574077246549023, 5)
        self.assertLess(hello.tan((np.pi)), 0.000000000000001)
        self.assertGreater(hello.tan((np.pi)), -0.000000000000001)

        with self.assertRaises(TypeError):
            hello.tan("hi")
        with self.assertRaises(TypeError):
            hello.tan('c')

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertAlmostEqual(hello.cot(1), 0.6420926159343306, 5)
        self.assertLess(hello.cot((np.pi)/2), 0.000000000000001)
        self.assertGreater(hello.cot((np.pi)/2), -0.000000000000001)

        with self.assertRaises(TypeError):
            hello.cot("hi")
        with self.assertRaises(TypeError):
            hello.cot('c')

if __name__ == "__main__":
    unittest.main()
