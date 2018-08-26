import math
print('''Написать функцию решения квадратного уравнения.  
		def solve_quadratic_equation(a, b, c): 
		# always returns 2(!) values: either 2 roots, 1 root and None or 2 Nones
 ''')

def solved_equation(a, b, c):
    print('Найдем решение квадратного уранвения: a*pow(x, 2) + b*x + c = 0')
    a = float(a)
    b = float(b)
    c = float(c)
    discriminant = pow(b, 2) - 4 * a * c
    print(discriminant)
    if discriminant == 0:
        x1 = ((-b + math.sqrt(Discriminant)) / (2 * a))
        print(x1)
        x2 = None
        return x1, x2
    if discriminant > 0:
        x1 = ((-b + math.sqrt(discriminant)) / (2 * a))
        x2 = ((-b - math.sqrt(discriminant)) / (2 * a))
        print(x1)
        print(x2)
        return x1, x2
    if discriminant < 0:
        x1 = None
        x2 = None
        return x1, x2



root_1, root_2 = solved_equation(input('Введите число а: '), input('Введите число b: '), input('Введите число c: '))

print('Roots of a given quadratic equation : %.4s, %.4s' % (root_1, root_2))
