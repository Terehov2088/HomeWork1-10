import random
("""Создайте список из всех нечётных чисел от 1 до 100 и передайте его в функцию, 
которая переставляет его элементы в случайном порядке 
(например, 99 11 43 19 … 7 91 3 1).
Примечание: использовать метод random.shuffle не допускается. 
""")



# list = [ i for i in range(1,101,2)]
# # list = random.sample(list, 50)
# # random.shuffle(a)  а так проще )
# print(list)
#
#
# def list_shuffle(list):
#     list1 = []
#     idx = 0
#     for elem in list:
#         el = random.choice(list)
#         for elem1 in list1:
#             if el == elem1:
#                 el = random.choice(list)
#         list1.insert(idx, el)
#         # print(list1)
#         idx += 1
#     list = list1
#     return list
#
#
# print(list_shuffle(list))


list = [ i for i in range(1,101,2)]
# list = random.sample(list, 50)
# random.shuffle(a)  а так проще )
print(list)


def list_shuffle(list):
    len1 = len(list)
    for _ in range(len1):
        i = random.randint(0, len1-1)
        j = random.randint(0, len1-1)
        list[i], list[j] = list[j], list[i]

    return list


print(list_shuffle(list))