import math
print('''Условия задачи 3: 
 Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости. Каждая окружность задается координатами центра и радиусом.
def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
''')

x1 = 5
x2 = 7
y1 = 5
y2 = 7
r1 = 15
r2 = 3

# что бы найти длину между центрами окружости, рассмотрим 2 прямоугольных треугольника и найдем их гипотенузы
dif_x = x2 - x1
print(dif_x)
x3 = dif_x / 2 # длина нижнего катета у обоих треугольников
x3_y1 = math.sqrt(pow(x3, 2) + pow(y1,2))
print(x3_y1) # гипотенуза 1 треугольника

x3_y2 = math.sqrt(pow(x3, 2) + pow(y2,2))
print(x3_y2) # гипотенуза 2 треугольника

# зная гипотенузы , найдем углы между гипотенузой и нижним катетом
cos_alfa_radians = x3 / x3_y1
print(cos_alfa_radians)
cos_alfa_degrees = int(math.acos(cos_alfa_radians) * 180 / math.pi)
print(cos_alfa_degrees) # угол первого треугольника

cos_beta_radians = x3 / x3_y2
print(cos_beta_radians)
cos_beta_degrees = int(math.acos(cos_beta_radians) * 180 / math.pi)
print(cos_beta_degrees) # угол второго треугольника

''' зная 2 угла прямоугольных треугольников, вычислим угол треугольника образующегося между центрами окружностей  
и общей точкой прямоугольных треугольников
'''
cos_delta = 180 - cos_alfa_degrees - cos_beta_degrees
print(cos_delta) # угол искомого треугольника

# зная 2 стороны и угол, найдем третью сторону треугольника и соответсвенно длину между центрами окружностей

z = math.sqrt((math.pow(x3_y1,2) + math.pow(x3_y2, 2) - 2 * x3_y1 *x3_y2 * math.cos(math.radians(cos_delta))))
print(z) # длина между центрами окружостей

# теперь вернемся к задаче определения пересикаются ли окружности


if z <= r1 + r2  and z >= math.fabs(r2 - r1):
    print('Окружности пересекаются')
else:
    print('Окружности не пересекаются')


