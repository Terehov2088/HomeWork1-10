import random
("""Написать функцию возвращающую наибольшую цифру случайно сгенерированного 12 ти-значного натурального числа.
 a) c использованием строк,
 b) без использования строк.
def get_max_digit(number): # returns int
""")


def get_max_digit1(number):
    biggest_number = 0
    number1 = (''.join([random.choice(str('0123456789')) for x in range(number)]))
    print(type(number1))
    number1 = int(number1)
    print('12 digit number: %d' % number1)

    biggest_number = number1 % 10
    number1 = number1 // 10
    for i in range(number):
        if number1 % 10 > biggest_number:
            biggest_number = number1 % 10
        number1 = number1 // 10
    return biggest_number

result = get_max_digit1(12)
print('Biggest number of 12 digit number is number: %d' % result)