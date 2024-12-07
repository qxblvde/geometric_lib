import math
import unittest

def area(r):
    '''
    Возвращает площадь круга с радиусом r.

        Args:
            r (int): десятичное целое число

        Returns:
            float: площадь круга, вычисляемая по формуле math.pi * r * r

        Example:
            print(area(5))  # Вывод: 78.53981633974483
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга с радиусом r.

        Args:
            r (int): десятичное целое число

        Returns:
            float: периметр круга, вычисляемый по формуле 2 * math.pi * r

        Example:
            print(perimeter(5)) # Вывод: 31.41592653589793
    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
        
    def test_float_area(self):
        res = area(5.5)
        self.assertAlmostEqual(res, 95.03317777109123, places=7)
       
    def test_area(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.53981633974483, places=7)

    def test_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 31.41592653589793, places=7)
        
    def test_float_perimeter(self):
        res = perimeter(5.5)
        self.assertAlmostEqual(34.55751918948772, places=7)
        
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

print(area(5.5))
print(perimeter(5.5))
