import random

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


print("""
Задача №10.  Для заданной матрицы (3*3) найти все ее седловые точки и вернуть список их координат (список списков).
Седловых точек может не быть, может быть 1 и более. Например, для матрицы ниже результат должен быть [[1, 0]]:
3  8  7
5  9  6     <--- седловая точка (1,0)
2  6  7
""")


matrix_random = [[random.randint(0, 9) for i in range(3)] for j in range(3)]
pretty_print_matrix(matrix_random)
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
saddle_elements(matrix_random)

print()

print("Задача №11. В двумерном списке (матрица=список списков) отсортировать четные столбцы по возрастанию, а нечетные - по убыванию.")

matrix_random = [[random.randint(0, 9) for i in range(3)] for j in range(4)]
print(pretty_print_matrix(matrix_random))
print("********===Начало функции===*********")


def col_sort(matrix):
    m = len(matrix)
    n = len(matrix[0])
    if n > m:
        delta = n - m
        len1 = (len(matrix) + delta)
    elif n < m:
        delta = m - n
        len1 = (len(matrix) - delta)
    elif n == m:
        len1 = (len(matrix))

    idx = 0
    matrix1 = []
    for i in range(len1):
        col = []
        for elem in matrix:
            col.append(elem[i])

        print('до %s' % col)
        if idx % 2 == 1:
            col.sort()
            print("posle %s" % col)
            matrix1.append(col)
            idx += 1
        else:
            col.sort(reverse=True)
            print("posle %s" % col)
            matrix1.append(col)
            idx += 1
    # print(pretty_print_matrix(matrix1))


    idx1 = 0
    for i in range(len(matrix)):
        for j in range(len1):
            matrix[i][j] = matrix1[j][i]
    idx1 +=1

    return matrix



print(col_sort(matrix_random))
print('==================')
pretty_print_matrix(matrix_random)