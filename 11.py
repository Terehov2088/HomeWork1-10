import math
print('''Условия задачи 3: 
 Написать функцию, которая будет переводить градусы в радианы (без использования math.radians). 
 Используя эту функцию, вывести на экран значения косинусов углов в 60, 45 и 40 градусов.
def degrees2radians(degrees): # returns float
''')


def degrees2radians(degrees):

    result_radians = degrees * math.pi/180
    return float(result_radians)



result_40 = degrees2radians(40)
result_45 = degrees2radians(45)
result_60 = degrees2radians(60)
print('Results: %.2f, %.2f, %.2f,' %  (result_40, result_45, result_60))
