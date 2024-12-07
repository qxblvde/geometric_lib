import unittest

def area(a, b):
    '''
    Возвращает площадь прямоугольника со сторонами a и b.

        Args:
            a (int): десятичное целое число
            b (int): десятичное целое число

        Returns:
            int: площадь прямоугольника, вычисляемая по формуле a * b

        Example:
            print(area(5, 3)) # Вывод: 15
    '''
    return a * b

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника со сторонами a и b.

        Args:
            a (int): десятичное целое число
            b (int): десятичное целое число

        Returns:
            int: периметр прямоугольника, вычисляемый по формуле (a + b) * 2

        Example:
            print(perimeter(5, 3)) # Вывод: 16
    '''
    return (a + b) * 2

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0) 
        self.assertEqual(res, 0)
        
    def test_float_area(self):
        res = area(5.5, 3)
        self.assertAlmostEqual(res, 16.5, places=7)
       
    def test_area(self):
        res = area(10, 10)  
        self.assertEqual(res, 100)

    def test_perimeter(self):
        res = perimeter(15, 10)
        self.assertEqual(res, 50)
        
    def test_float_perimeter(self):
        res = perimeter(5.5, 3)
        self.assertAlmostEqual(res, 17.0, places=7)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
print(area(5.5, 3))
print(perimeter(5.5, 3))

