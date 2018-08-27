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
    print('12 digit number: %s' % number1)

    for char in number1:
        char = int(char)
        print(char)
        if char > biggest_number:
            biggest_number = char
    return biggest_number

result = get_max_digit1(12)
print('Biggest number of 12 digit number is number: %d' % result)


