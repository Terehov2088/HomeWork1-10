# class Student:
#     TASKS_NUM = 37
#     TEST_WEIGHTS = [1, 1, 1, 2, 2, 2, 4, 4, 4, 8, 8, 15]
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.hw_tasks = {i:0 for i in range(1, self.TASKS_NUM+1)}
#         self.tests = [0]*len(self.TEST_WEIGHTS)
#
#
#     def pretty_print(self):
#         print('Name:', self.name)
#         print('Age:', self.age)
#         print('Rank:', self.total_rank())
#
#     def accept_task(self, num_task):
#         self.hw_tasks[num_task] = 1
#
#     def total_rank(self):
#         total_rank = 0
#         for key in self.hw_tasks:
#             total_rank += self.hw_tasks[key]
#
#         for i in range(len(self.tests)):
#             test = self.tests[i]
#             weight_coeff = self.TEST_WEIGHTS[i]
#             total_rank += test * weight_coeff
#         return total_rank
#
#     def accept_test(self, num_test):
#         self.tests[num_test-1] = 1
#
#
#
#
# student1 = Student('Alice', 22)
# # student2 = Student('Bob', 42)
# # student3 = Student('Kate', 18)
# student1.accept_task(1)
# print('=============')
# student1.pretty_print()
# # print('=============')
# # student2.pretty_print()
# # print('=========***====')
#
#
#
# # student3.accept_task(1)
# # student3.accept_test(12)
# #
# # student3.pretty_print()


"""
Задача 34. Создать класс Годзилла. При создании Годзиллы указывается объем желудка. 
Написать для данного класса метод поедания людей eat. 
В данный метод должен передаваться объем съеденного человека и соответственно уменьшаться место в желудке.
 Когда Годзилла заполнит желудок на 90%, то Годзилла должен говорить он наелся и больше не может поедать людей.
"""
import math

class Godzilla():
    AGE_OF_ADULT_GODZILLA = 6


    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.fill_stomach = [0] * math.ceil(int((self.stomach_value() / 75) + self.age/2))  #будем считать, что средний вес поедаемого студента  75 кг
        # print(self.fill_stomach)
        # print(self.fill_stomach.count(0))
        # print(len(self.fill_stomach))

    def pretty_print(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('Stomach_value:', self.stomach_value())
        print('Fill_stomach:', self.filled_stomach())
        # print('Godzilla say:', self.godzilla_full())  # хотел сделать метод который выводил бы сообщение после того как будет указана текущее заполнение желудка, но пока никак не получилось

    def stomach_value(self):
        if self.age <= self.AGE_OF_ADULT_GODZILLA:
            stomach_value = int(math.exp(self.age))
        elif self.age > self.AGE_OF_ADULT_GODZILLA:
            stomach_value = int(math.exp(self.AGE_OF_ADULT_GODZILLA) + (math.exp(self.AGE_OF_ADULT_GODZILLA-1)* self.age))
        return stomach_value


    def godzilla_eat(self, mass):
        a = len(self.fill_stomach)
        for i in range(a):
            if self.fill_stomach[i] == 0:
                self.fill_stomach[i] = mass
                break


    def filled_stomach(self):
        filled_stomach = 0
        for elem in self.fill_stomach:
            if filled_stomach < int(self.stomach_value() * 90 / 100) and (filled_stomach+elem) <= int(self.stomach_value() * 90 / 100):
                filled_stomach += elem
            else:
                print("Годзилла %s наелся, и больше не может жрать студентов которые не сделали ДЗ" % self.name)
                return filled_stomach
        print("Годзилла %s не сытый, и еще может жрать студентов которые не сделали ДЗ" % self.name)
        return filled_stomach




    # def godzilla_full(self):
    #     if self.filled_stomach()
    #     # if self.filled_stomach() < int(self.stomach_value() * 90 / 100):
    #         print("Годзилла %s наелся, и больше не может жрать студентов которые не сделали ДЗ" % self.name)
    #     else:
    #         print("Годзилла %s не сытый, и еще может жрать студентов которые не сделали ДЗ" % self.name)





godzilla1 = Godzilla('Morty', 10)
godzilla1.godzilla_eat(850)
godzilla1.godzilla_eat(50)
godzilla1.godzilla_eat(880)

godzilla2 = Godzilla("Rik", 20)
godzilla2.godzilla_eat(1000)
godzilla2.godzilla_eat(1000)

godzilla1.pretty_print()
print("=================")
godzilla2.pretty_print()
