import unittest
import circle
import rectangle
import square
import triangle

class TestCircle(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = circle.area(5)
        self.assertAlmostEqual(res, 78.53981633974483, places=7)

    def test_perimeter(self):
        res = circle.perimeter(5)
        self.assertAlmostEqual(res, 31.41592653589793, places=7)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

class TestRectangle(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_perimeter(self):
        res = rectangle.perimeter(15, 10)
        self.assertEqual(res, 50)

    def test_zero_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

class TestSquare(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = square.area(15)
        self.assertEqual(res, 225)

    def test_perimeter(self):
        res = square.perimeter(5)
        self.assertEqual(res, 20)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

class TestTriangle(unittest.TestCase):
    def test_zero_area(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)

    def test_area(self):
        res = triangle.area(15, 2)
        self.assertEqual(res, 15)

    def test_perimeter(self):
        res = triangle.perimeter(5, 5, 6)
        self.assertEqual(res, 16)

    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)
