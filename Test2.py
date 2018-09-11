import random



"""
Задача №10. Для заданной матрицы (3*3) найти все ее седловые точки и вернуть список их координат (список списков).
Седловых точек может не быть, может быть 1 и более. Например, для матрицы ниже результат должен быть [[1, 0]]:
3  8  7
5  9  6     <--- седловая точка (1,0)
2  6  7
"""
matrix_random = [[random.randint(0, 9) for i in range(3)] for j in range(3)]
print(pretty_print_matrix(matrix_random))
print("********===Начало функции===*********")

def saddle_elements(matrix):
    idx1 = 0
    idx2 = 0

    for elem in matrix:
        print("Минимальный элемент строки %s равен %s" % (elem, min(elem)))
        print("Колличество минимальных элементов в строке %s" % elem.count(min(elem)))

        if elem.count(min(elem)) == 1:
            m = elem.index(min(elem))
            print("Позицию минимального элемента строки %s" % m)
            col = []
            for elem1 in matrix:
                col.append(elem1[m])
            print(col)
            print("Максимальный элемент столбца %s равен %s" % (col, max(col)))
            print("Колличество максимальных элементов в столбце %s" % col.count(max(col)))
            m1 = col.index(max(col))
            print("Позицию максимального элемента строки %s" % m1)
            print('********************')

            if col.count(max(col)) == 1 and min(elem) == max(col):
                result = [m1, m]
                idx1 += 1

        if idx1 > idx2:
            idx2 = idx1
            result1 = []
            result1.append(result)

    if idx1 == 0:
        print('Седальных точек нет')
    else:
        print('Координаты седальной точки: %s' % result1)
        return result1
print(saddle_elements(matrix_random))




"Задача №11. В двумерном списке (матрица=список списков) отсортировать четные столбцы по возрастанию, а нечетные - по убыванию."

matrix_random = [[random.randint(0, 9) for i in range(3)] for j in range(3)]
print(pretty_print_matrix(matrix_random))
print("********===Начало функции===*********")


def saddle_elements(matrix):
   matrix1 = []
   for i in range(len(matrix)):
       col = []
       for elem in matrix:
           col.append(elem[i])
       print('до %s' % col)
       if i % 2 == 1:
           col.sort()
           print("posle %s" % col)
           matrix1.append(col)
       else:
           col.sort(reverse=True)
           print("posle %s" % col)
           matrix1.append(col)
   # print(pretty_print_matrix(matrix1))

   for i in range(len(matrix)):
       for j in range(len(matrix[i])):
           matrix[i][j] = matrix1[j][i]
   return matrix



print(saddle_elements(matrix_random))
print('==================')
print(pretty_print_matrix(matrix_random))