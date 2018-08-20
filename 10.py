import math
print('Hello Dmitriy')
print( )


print('''Условия задачи: 
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

leo_tolstoy = 'Leo Tolstoy*1828-08-28*1910-11-20'
leo_tolstoy_split = leo_tolstoy.split("*")

leo_tolstoy_name = str(leo_tolstoy_split[0])
leo_tolstoy_born = str(leo_tolstoy_split[1])
leo_tolstoy_death = str(leo_tolstoy_split[2])

leo_tolstoy_born_split = (leo_tolstoy_born.split('-'))
leo_tolstoy_death_split = (leo_tolstoy_death.split('-'))

leo_tolstoy_born_year = int(leo_tolstoy_born_split[0])
leo_tolstoy_death_year = int(leo_tolstoy_death_split[0])

leo_tolstoy_live = int(math.fabs(leo_tolstoy_death_year - leo_tolstoy_born_year))


print('%s, %s ' % (leo_tolstoy_name, leo_tolstoy_live))


marc = 'Marcus Aurelius*121-04-26*180-03-17'
marc_split = marc.split("*")

marc_name = str(marc_split[0])
marc_born = str(marc_split[1])
marc_death = str(marc_split[2])

marc_born_split= (marc_born.split('-'))
marc_death_split = (marc_death.split('-'))

marc_born_year = int(marc_born_split[0])
marc_death_year = int(marc_death_split[0])

marc_live = int(math.fabs(marc_death_year - marc_born_year))


print('%s, %s ' % (marc_name,marc_live))
