import math
print('''Условия задачи 3: 
 Написать функцию, которая вычислит площадь и объем конуса по его радиусу и высоте. 
 Результат работы функции должен вернуть два значения.
def cone_square_and_volume(radius, height): # returns 2 floats
''')

def cone_square_and_volume(radius, height):

    radius = int(radius)
    height = int(height)
    cone_volume = height/3 * math.pi * math.pow(radius, 2)
    generatrix = math.sqrt(math.pow(radius, 2) + math.pow(height, 2))
    cone_square = math.pi * radius * (radius + generatrix)
    return cone_volume, cone_square

cone_volume, cone_square = cone_square_and_volume (input('Введите радиус: '),input('Введите высоту: '))

print('Results: %.5f, %.5f' % (cone_square, cone_volume))