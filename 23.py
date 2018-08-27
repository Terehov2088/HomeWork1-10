import math
import random
('''Согласно древней индийской легенде создатель шахмат за своё изобретение попросил у раджи незначительную, 
на первый взгляд, награду: столько пшеничных зёрен, сколько окажется на шахматной доске, 
если на первую клетку положить одно зерно, на вторую — два зерна, на третью — четыре зерна и т. д. 
Оказалось, что такого количества зерна нет на всей планете (оно равно 2**64 − 1 зерен). 
Посчитайте, начиная с какой клетки по счету, общее количество зерен, которое должен был бы отдать раджа изобретателю было больше 1 000 000 зерен 
и сколько конкретно зерен он должен был бы отдать.
     def chess_reward(): # returns 2 ints (cell number and total number of corns)
		pass 
''')


def chess_reward(cell_number, total_number_of_corns):

    inventor_price = 1
    counter = 1
    while counter <= cell_number:
        inventor_price += math.pow(2, counter)
        counter += 1
        if inventor_price > total_number_of_corns:
            return counter, inventor_price

result1, result2 = chess_reward(64, 1000000)
print('The number of corns will be more than one million in: %d cell and the total number of cornss that the inventor won: %d corn ' % (result1,result2))