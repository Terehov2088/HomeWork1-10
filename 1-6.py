import math
print('Hello Dmitriy')
print( )

print('''Необходимо решить ряд математических задач.
Условия задач: 
Задача1: Найти результат выражения для произвольных значений a,b,c: a + b * ( c / 2 )
Задача2: Найти результат выражения для произвольных значений a,b: (a2 + b2) % 2
Задача3: Найти результат выражения для произвольных значений a,b,c: ( a + b ) / 12 * c % 4 + b
Задача4: Найти результат выражения для произвольных значений a,b,c: (a - b * c ) / ( a + b ) % c
Задача5: Найти результат выражения для произвольных значений a,b,c: | a - b | /( a + b)3 - cos( c )
Задача6: Найти результат выражения для произвольных значений a,b,c: ( ln( 1 + c ) / -b )4+ | a |
''')

print('Решение:')
print('Определим значение переменны a,b,c:')

a = 8
b = 16
c = 11

print('Решение задачи №1:')
print('Подставив наши переменные в мат. выражение: z1 = a + b * (c/2)')
z1 = a + b * (c/2)
print('Ответ: z1=', z1)

print( )
print('Решение задачи №2:')
print('Подставив наши переменные в мат. выражение: z2 = math.fmod((math.pow(a,2)+b**2),2)')
z2 = (math.pow(a, 2)+ b**2) / 2
print('Ответ: z2=',z2)

print( )
print('Решение задачи №3:')
print('Подставив наши переменные в мат. выражение: z3 = (a+b) / 12 * (c % 4) + b')
z3 = (a+b) / 12 * (c % 4) + b
print('Ответ: z3=',z3)

print( )
print('Решение задачи №4:')
print('Подставив наши переменные в мат. выражение: z4 = ((a - b * c) / (a + b)) % c')
z4 = ((a - b * c) / (a + b)) % c
print('Ответ: z4=',z4)

print( )
z5 = math.fabs(a - b) / math.pow((a + b), 3) - math.cos(c)
print('Решение задачи №5:')
print('Подставив наши переменные в мат. выражение: z5 = math.fabs(a - b) / math.pow((a + b), 3) - math.cos(c)')
z5 = math.fabs(a - b) / math.pow((a + b), 3) - math.cos(c)
print('Ответ: z5=',z5)

print( )

print('Решение задачи №6:')
print('Подставив наши переменные в мат. выражение: z6 = math.pow((math.log( 1 + c ) / -b ), 4) + math.fabs(a)')
z6 = math.pow((math.log( 1 + c ) / -b ), 4) + math.fabs(a)
print('Ответ: z6=',z6)

print()
print('Решив все шесть задач мы получили следующие ответы:')
print('Ответ задача1:', z1)
print('Ответ задача2:', z2)
print('Ответ задача3:', z3)
print('Ответ задача4:', z4)
print('Ответ задача5:', z5)
print('Ответ задача6:', z6)
print()
