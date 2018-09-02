import random
("""Написать функцию возвращающую наибольшую цифру случайно сгенерированного 12 ти-значного натурального числа.
 a) c использованием строк,
 b) без использования строк.
def get_max_digit(number): # returns int
""")


def get_max_digit1(number):
    biggest_number = 0

    print('12 digit number: %d' % number)

    biggest_number = number % 10
    number = number // 10
    while number > 0:
        if number % 10 > biggest_number:
            biggest_number = number % 10
        number = number // 10
        print(number)
    return biggest_number


number = (''.join([random.choice(str('0123456789')) for x in range(5)]))
print(type(number))
number = int(number)

result = get_max_digit1(number)
print('Biggest number of 12 digit number is number: %d' % result)