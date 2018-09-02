import random
("""Создайте список из всех нечётных чисел от 1 до 100 и передайте его в функцию, 
которая переставляет его элементы в случайном порядке 
(например, 99 11 43 19 … 7 91 3 1).
Примечание: использовать метод random.shuffle не допускается. 
""")



list = [ i for i in range(1,101,2)]
# random.shuffle(a)  а так проще )
print(list)


def list_shuffle(list):
    list1 = []
    sum = 0
    for elem in list:
        el = random.choice(list)
        for elem1 in list1:
            if el == elem1:
                el = random.choice(list)
        list1.insert(sum, el)
        # print(list1)
        sum += 1
    list = list1
    return list


print(list_shuffle(list))