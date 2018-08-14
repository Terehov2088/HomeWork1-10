import math
print('Hello Dmitriy')
print( )


print('''Условия задачи 3: 
 Дана строка вида 'Leo Tolstoy*1828-08-28*1910-11-20'. 
 В этой строке указаны имя писателя и через символ * даты рождения и смерти. 
 Даты указаны в формате "YYYY-MM-DD". Требуется написать программу, 
 которая по переданной строке определит возраст писателя и распечает его имя и возраст. 
 Например, для строки 'Leo Tolstoy*1828-08-28*1910-11-20' программа должна распечает: 'Leo Tolstoy, 82'. 
 Для строки 'Marcus Aurelius*121-04-26*180-03-17' - 'Marcus Aurelius, 59'. 
 Примечание: Т.к. имена писателей могут быть разной длины, то индексы символов разделителей ('*', '-') будут разными! 
 Месяцы и дни для определения возраста можно игнорировать
''')

print('Решение:')

Leo_tolstoy = 'Leo Tolstoy*1828-08-28*1910-11-20'
Leo_tolstoy_split = Leo_tolstoy.split("*")

Leo_tolstoy_name = str(Leo_tolstoy_split[0])
Leo_tolstoy_born = str(Leo_tolstoy_split[1])
Leo_tolstoy_death = str(Leo_tolstoy_split[2])

Leo_tolstoy_born_split = (Leo_tolstoy_born.split('-'))
Leo_tolstoy_death_split = (Leo_tolstoy_death.split('-'))

Leo_tolstoy_born_year = int(Leo_tolstoy_born_split[0])
Leo_tolstoy_death_year = int(Leo_tolstoy_death_split[0])

Leo_tolstoy_live = int(math.fabs(Leo_tolstoy_death_year - Leo_tolstoy_born_year))


print('%s, %s ' % (Leo_tolstoy_name,Leo_tolstoy_live))


Marc = 'Marcus Aurelius*121-04-26*180-03-17'
Marc_split = Marc.split("*")

Marc_name = str(Marc_split[0])
Marc_born = str(Marc_split[1])
Marc_death = str(Marc_split[2])

Marc_born_split= (Marc_born.split('-'))
Marc_death_split = (Marc_death.split('-'))

Marc_born_year = int(Marc_born_split[0])
Marc_death_year = int(Marc_death_split[0])

Marc_live = int(math.fabs(Marc_death_year - Marc_born_year))


print('%s, %s ' % (Marc_name,Marc_live))
