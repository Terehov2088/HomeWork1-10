import random
("""Создайте список из 11 случайных целых чисел из отрезка [-1;1]. 
Передайте его в функцию, которая определит какой элемент встречается в списке чаще всего и вернет этот элемент. 
Однако, если два каких-то элемента встречаются одинаковое количество раз, 
то вернуть None, а не самый часто встречающийся элемент, даже если дублирующиеся элементы не максимальны!
     def calc_frequency(lst): # returns the most frequent number or None
	Например:
		для [1, 1, 1, -1, -1, 1, 1, -1, 0, 0, 0] надо вернуть None
		для [1, 1, 1, 1, -1, 1, 1, -1, 0, 0, 0] надо вернуть 1
 """)


list = [random.randint(-1, 1) for i in range(11)]
print(list)

def calc_frequency(list):
    sum_1 = 0
    sum_2 = 0
    sum_3 = 0
    el1 = -1
    el2 = 0
    el3 = 1

    for i in list:
        if i == -1:
            sum_1 +=1
        elif i == 0:
            sum_2 +=1
        elif i == 1:
            sum_3 +=1
    print("Sum_1 %s " % sum_1)
    print("Sum_2 %s " % sum_2)
    print("Sum_3 %s " % sum_3)
    if sum_1 > sum_2 and sum_1 > sum_3:
        if sum_3 == sum_2:
            return None
        else:
            return el1
    elif sum_2 > sum_1 and sum_2 > sum_3:
        if sum_1 == sum_3:
            return None
        else:
            return el2
    elif sum_3 > sum_1 and sum_3 > sum_2:
        if sum_2 == sum_1:
            return None
        else:
            return el3


result = calc_frequency(list)
print(result)
print("The most common element: %.4s " % result)
