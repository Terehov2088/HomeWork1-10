print('Hello Dmitriy')
print( )

print('''Необходимо решить ряд задач.
Условия задачи 1: 
Задача1: Преобразовать строку с американским форматом даты в европейский. 
Например, '05.17.2016' преобразуется в '17.05.2016
''')
print()

print('Решение задачи №1:')
print('Вариант 1:')
american_data = '05.17.2016'

american_data_split = american_data.split(".")

day = int(american_data_split[0])
month = int(american_data_split[1])
year = int(american_data_split[2])

print('\n Европейская дата будет выглядеть так: %d.%d.%d ' %
      (month, day, year))
print()

print('Вариант 2:')
american_data = '05.17.2016'

print('\n Европейская дата будет выглядеть так: %s.%s.%s ' %
      (american_data[3:5], american_data[0:2], american_data[6:10]))
print()

print('Вариант 3:')
american_data = '05.17.2016'
europe_data = '17.05.2016'

american_data_split = american_data.split(".")

day = str(american_data_split[0]) + ('.')
month = str(american_data_split[1]) + ('.')
year = str(american_data_split[2])

american_data_result = month + day + year
print('\n Европейская дата будет выглядеть так:', american_data_result)
print()
print('Бонус плюс на барабане: ')
if american_data_result == europe_data:
    print('Строки одинаковы')
else:
    print("Строки не одинаковы")
print()

print('''Условия задачи 2: 
 Дана строка с именем студента, в которой имя предшествует фамилии, например  ‘Mark Zuckerberg‘. 
Написать программу, которая преобразует эту строку, ставя фамилию на первое место, а имя на второе. 
Т.е. ‘Mark Zuckerberg‘ -> ‘Zuckerberg Mark‘.
''')

print('Решение задачи №2:')
print('Введите данные в формате: Имя Фамилия')
name_surname = str(input('Поле ввода:'))

name_surname_split = name_surname.split(" ")

name = name_surname_split[0]
surname = name_surname_split[1]
space = (" ")
surname_name = (surname + space + name)
print('Имя и фамилия студента', name_surname)
print('Конвертируется в:')
print("Фамилию и имя студента:", surname_name)
print()


