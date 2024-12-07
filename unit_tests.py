import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
import unittest
import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_area(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.53981633974483, places=7)

    def test_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 31.41592653589793, places=7)
        
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
        
class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0) 
        self.assertEqual(res, 0)
       
    def test_square_area(self):
        res = area(10, 10)  
        self.assertEqual(res, 100)

    def test_square_perimeter(self):
        res = perimeter(15, 10)
        self.assertEqual(res, 50)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
        
class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_square_area(self):
        res = area(15)
        self.assertEqual(res, 225)

    def test_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)
        
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)
       
    def test_area(self):
        res = area(15, 2)
        self.assertEqual(res, 15)

    def test_perimeter(self):
        res = perimeter(5, 5, 6)
        self.assertEqual(res, 16)
        
    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
