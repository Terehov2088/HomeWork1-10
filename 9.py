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

snake_employee = str(snake_split[0])
snake_first = str(snake_split[1])
snake_name = str(snake_split[2])

camel_case = (snake_employee.title() + snake_first.title() + snake_name.title())
print('Формат snake_case ', snake_case)
print('Конвертируется в:')
print("Формат CamelCase:", camel_case)
print()