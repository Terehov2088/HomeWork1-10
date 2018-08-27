import random
("""Написать функцию возвращающую наибольшую цифру случайно сгенерированного 12 ти-значного натурального числа.
 a) c использованием строк,
 b) без использования строк.
def get_max_digit(number): # returns int
""")


def get_max_digit1(number):
    biggest_number = 0

    for char in number:
        char = int(char)
        if char > biggest_number:
            biggest_number = char
    return biggest_number


number = (''.join([random.choice(str('0123456789')) for x in range(12)]))
print(type(number))


print('12 digit number: %s' % number)
result = get_max_digit1(number)
print('Biggest number of 12 digit number is number: %d' % result)


