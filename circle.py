import math


def area(r):
	'''
	Возвращает площадь круга с радиусом a.

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
	Возвращает периметр круга с радиусом a.

		Args:
			r (int): десятичное целое число

		Returns:
			float: периметр круга, вычисляемый по формуле 2 * math.pi * r

		Example:
                        print(perimeter(5)) # Вывод: 31.41592653589793
	'''
	return 2 * math.pi * r

