
print('''Условия задачи 3: 
 Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа, 
 введенного пользователем в консоли, без использования операторов цикла. 
 a) cо строками, б) без использования строк.
def sum_of_digits(number): # returns int
''')

def sum_of_digits(number):
    digit_1 = int(number[0])
    digit_2 = int(number[1])
    digit_3 = int(number[2])
    result_sum = digit_1 + digit_2 + digit_3
    return result_sum

result = sum_of_digits(input('Введите трехзначное число:'))
print(result)

def sum_of_digits_1(number_1):
    number_1 = int(number_1)
    digit_1 = number_1 % 10
    number_1 = number_1 // 10
    digit_2 = number_1 % 10
    number_1 = number_1 // 10
    digit_3 = number_1 % 10
    result_sum = digit_1 + digit_2 + digit_3
    return result_sum

result = sum_of_digits_1(input("Введите трехзначное число:"))
print(result)