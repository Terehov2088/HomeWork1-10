print('''Условия задачи: 
 Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути. Через 4 км пути первый поезд
может свернуть на запасной путь. При заданных скоростях узнать столкнутся ли поезда.
def have_trains_crashed(v1, v2): # returns boolean value ''')


def have_trains_crashed(v1, v2):
    t = 1
    if v1 * t <= 4 and v2 * t >= 6:
        return True
    else:
        return False

if have_trains_crashed(1, 1):
        print('Поезда столкнутся')
else:
        print('Поезда не столкнутся')
