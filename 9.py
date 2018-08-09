print('Hello Dmitriy')
print( )


print('''Условия задачи 3: 
 Написать программу, которая преобразует имя переменной в формате snake_case в формат CamelCase. 
 Для простоты считаем, что имя переменной всегда состоит из 3-х слов. 
 Например: 'employee_first_name' -> 'EmployeeFirstName'
''')

print('Решение задачи №3:')
print('Введите данные в формате: employee_first_name')
snake_case = str(input())

sp = snake_case.split("_")

s1 = str(sp[0])
s2 = str(sp[1])
s3 = str(sp[2])

CamelCase = (s1.title() + s2.title() + s3.title())
print('Формат snake_case ', snake_case)
print('Конвертируется в:')
print("Формат CamelCase:", CamelCase)
print()