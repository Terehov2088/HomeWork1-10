print('Hello Dmitriy')
print( )


print('''Условия задачи 3: 
 Написать программу, которая преобразует имя переменной в формате snake_case в формат CamelCase. 
 Для простоты считаем, что имя переменной всегда состоит из 3-х слов. 
 Например: 'employee_first_name' -> 'EmployeeFirstName'
''')

print('Решение задачи №3:')
print('Введите данные в формате: employee_first_name')
snake_case = str(input("Поле ввода:"))

snake_split = snake_case.split("_")

snake_1 = str(snake_split[0])
snake_2 = str(snake_split[1])
snake_3 = str(snake_split[2])

Camel_case = (snake_1.title() + snake_2.title() + snake_3.title())
print('Формат snake_case ', snake_case)
print('Конвертируется в:')
print("Формат CamelCase:", Camel_case)
print()