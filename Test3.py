import random
import math
import string
print("""Задача №12.  Для проверки остаточных знаний учеников после летних каникул,
учитель младших классов решил начинать каждый урок с того, чтобы задавать каждому ученику пример из таблицы умножения, 
но в классе 15 человек, а примеры среди них не должны повторяться. В помощь учителю напишите программу, 
которая будет выводить на экран 15 случайных примеров из таблицы умножения 
(от 2*2 до 9*9, потому что задания по умножению на 1 и на 10 — слишком просты). 
При этом среди 15 примеров не должно быть повторяющихся (примеры 2*3 и 3*2 и им подобные пары считать повторяющимися)
""")
def pretty_print_matrix(matrix):

    def find_max(matrix):
        max = matrix[0][0]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if max < matrix[i][j]:
                    max = matrix[i][j]
        return max

    formatter = "%%%dd" % (len(str(find_max(matrix)))+1)


    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(formatter % matrix[i][j], end="")
        print()



multiplication_table = [[(i+1)*(j+1) for i in range(10)] for j in range(10)]
pretty_print_matrix(multiplication_table)
print()
example_table = [[0 for i in range(3)] for j in range(15)]
pretty_print_matrix(example_table)
print()
def multiplication_example(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])-1):
            matrix[i][j] = random.randint(2, 9)

        matrix[i][j+1] = (matrix[i][j])*(matrix[i][j-1])
    pretty_print_matrix(matrix)

    for elem in matrix:
        for i in range((len(elem)-1), len(elem) ):
            if matrix[elem.index(elem)][i] ==







    return 0



multiplication_example(example_table)



# def find_saddle_points(a):
#   """Finds saddle points in a, a 2 dimensional array.
#
#   Args:
#     a: A 2 dimensional array in row-major (y, x) order.
#   Returns:
#     A list of (x, y) location of the saddle points.
#   """
#   # Holds a (value, column) tuple of the min value and its column for each row.
#   row_mins = [min((a[row][col], col) for col in range(len(a[row]))) for row in range(len(a))]
#   # Holds a (value, row) tuple of the max value and its row for each column.
#   col_maxes = [max((a[row][col], row) for row in range(len(a))) for col in range(len(a[0]))]
#
#   ret = []
#   for row, (row_min, col) in enumerate(row_mins):
#     if col_maxes[col][1] == row:
#       ret.append((row, col))
#       print('Координаты седальной точки: %s' % ret)
#   return ret
# find_saddle_points(matrix_random)