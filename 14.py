print('''Условия задачи : 
 Написать функцию, которая будет проверять четность некоторого числа.
		def is_even(number): # returns boolean value
			pass
''')

def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

var = even(int(input('Введите число: ')))
if var:
    print('Число четное')
else:
    print('Число не четное')