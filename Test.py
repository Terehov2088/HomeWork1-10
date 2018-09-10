import math
import random
import string

"""Задача №1,2,3 
1. (a + b * c)2                  
2. a - 4 * b / c                                   
3. (a * b + 4) / (c - 1)  по 1 баллу"""

# a = 10
# b = 3
# c = 5
#
# print(math.pow((a + b * c), 2))
# print(a - 4 * b / c)
# print((a * b +4) / (c - 1))

"Задача №4. Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры. 2 балла"

# number = input("Введите 5-ти значное число: ")
# multiply = 1
# for i in number:
#     if (int(i) % 2) == 1:
#         multiply *= int(i)
# print(multiply)

"Задача №5. Создать программу, выводящую на экран ближайшее к 10 из двух чисел, введенных пользователем. Например, среди чисел 8,5 и 11,45 ближайшее к десяти 11,45. 2 балла"

# number1 = float(input("Введите первое число: "))
# number2 = float(input("Введите второе число: "))
#
# if math.fabs(number1 - 10) == math.fabs(number2 - 10):
#     print("Число %.2f, ,находится к числу 10.00, на том же удалении, что и число %.2f" % (number2, number1))
# elif math.fabs(number1 - 10) < math.fabs(number2 - 10):
#     print("Число %.2f, ,ближе к числу 10.00, чем число %.2f" % (number1,number2))
# else:
#     print("Число %.2f, ,ближе к числу 10, чем число %.2f" % (number2, number1))


"""
Задача №6. Определить является ли строка изограммой (https://en.wikipedia.org/wiki/Isogram )
т.е. что все буквы в ней за исключением пробелов встречаются только один раз. 
Например, строки 'Питон', 'downstream', 'книга без слов' являются изограммами, а само слово 'изограмма' - нет. 2 балла"""


# text = input("Введите текст: ")
# def isogram(text):
#     for char in text:
#         if char in string.punctuation or char == " ":
#             continue
#         else:
#             sum = text.count(char)
#
#             if sum > 1:
#                 return False
#     return True
#
#
#
#
#
# result = isogram(text)
# if result == True:
#     print("Строка является изограммой")
# else:
#     print("Строка не является изограммой")



"Задача №7. Найти сумму десяти первых чисел ряда Фибоначчи. 4 балла"
# n = int(input("Введите сумму скольких числ ряда фибоначчи вы хотите найти: "))
#
#
# def fibonacci_sum(n):
#     sum_n = 2
#     fib_sum = 0
#     fib1 = 1
#     fib2 = 1
#     i = 2
#     while i < n:
#         sum_n = sum_n + fib_sum
#         fib_sum = fib2 + fib1
#         fib1 = fib2
#         fib2 = fib_sum
#         i += 1
#     sum_n = sum_n + fib2
#     return sum_n
#
#
# print("Сумма первых %d чисел ряда фибоначчи равна %d " % (n, fibonacci_sum(n)))


# n1 = int(input("Введите от какого числа фибоначчи будет расчитываться сумма ряда: "))
# n2 = int(input("Введите до какого числа фибоначчи будет расчитываться сумма ряда: "))
#
#
# def fibonacci_delta(n1):
#     fib_sum = 0
#     fib1 = 1
#     fib2 = 1
#     i = 2
#     while i < n1 + 1:
#         fib_sum = fib2 + fib1
#         fib1 = fib2
#         fib2 = fib_sum
#         i += 1
#     return fib1, fib2
#
#
# def fibonacci_sum(fib1, fib2 ,n1, n2):
#     sum_n = fib1 + fib2
#     fib_sum = 0
#     i = n1 + 1
#     while i < n2:
#         sum_n = sum_n + fib_sum
#         fib_sum = fib2 + fib1
#         fib1 = fib2
#         fib2 = fib_sum
#         i += 1
#     sum_n = sum_n + fib2
#     return sum_n
#
# fib1, fib2 = fibonacci_delta(n1)
# print("Сумма последовательности ряда фибоначчи с %d числа, по %d число  равна %d " % (n1, n2, fibonacci_sum(fib1, fib2, n1, n2)))


"Задача №8. 8. В одномерном списке поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах. *IN PLACE* 4 балла"


# list = [random.randint(1, 100) for i in range(0, 20)]
# print("Исходный список: %s " % list)
#
# id_max = (list.index(max(list)))
# id_min = (list.index(min(list)))
#
#
# list[id_max], list[id_min] = list[id_min], list[id_max]
# print("Изменен. список: %s " % list)


'''Задача №9. Нормировать одномерный список случайных чисел. Нормирование означает приведение всех значений массива к интервалу [-1;1], 
причем максимальное абсолютное значение элементов после нормирование должно быть равно 1. Например, последовательность [-5, 3, 4] после нормирование будет выглядеть [-1, 0.6, 0.8]'''

# list = [random.randint(-100, 100) for i in range(0, 20)]
# print(list)
#
# list_max = max(list)
# list_min = min(list)
# if abs(list_max) > abs(list_min):
#     normalize = list_max
# else:
#     normalize = list_min
# print(normalize)
#
# new_list = []
# for elem in list:
#     elem = elem / abs(normalize)
#     new_list.append(elem)
# new_list.sort()
# print(new_list)
