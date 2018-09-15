import random
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
print()


def summer_test():
    matrix = [[0 for i in range(3)] for j in range(15)]
    for i in range(len(matrix)):
        end = True
        while end == True:
            for j in range(len(matrix[i]) - 1):
                matrix[i][j] = random.randint(2, 9)
            matrix[i][j + 1] = (matrix[i][j]) * (matrix[i][j - 1])
            end = False
            elem = matrix[i][j + 1]
            idx = 0
            for k in range(len(matrix)):
                if elem == matrix[k][j + 1]:
                    idx +=1
            if idx > 1:
                end = True

    lst = [str(elem[0]) + '*' + str(elem[1]) for elem in matrix]
    return lst


print(summer_test())



