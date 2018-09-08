("""
30. Написать функцию, возвращающую все простые числа от 1 до 100 в виде списка.

def gen_primes(): # returns list of ints
""")



n = int(input("Введите колличество чисел: "))


# def gen_primes(n):
#     natural_numbers = list(range(2, n + 1))
#     for number in natural_numbers:
#         if number != 0:
#             for candidate in range(2 * number, n + 1, number):
#                 natural_numbers[candidate - 2] = 0
#     primes = [number for number in natural_numbers if number != 0]
#     return primes
#
# print(gen_primes(n))


# natural_numbers = list(range(2, n + 1))
#
# for number in natural_numbers:
#     if number != 2:
#         if number % 2 == 0:
#             natural_numbers.remove(number)
#
# for number in natural_numbers:
#     if number != 3:
#         if number % 3 == 0:
#             natural_numbers.remove(number)
#
#
# for number in natural_numbers:
#     if number != 5:
#         if number % 5 == 0:
#             natural_numbers.remove(number)
#
# for number in natural_numbers:
#     if number != 7:
#         if number % 7 == 0:
#             natural_numbers.remove(number)
#
# for number in natural_numbers:
#     if number != 11:
#         if number % 11 == 0:
#             natural_numbers.remove(number)
#
# print(natural_numbers)


def gen_sundaram(n):
    primes = []
    natural_numbers = [0] * n

    i = k = j = 0
    while 3 * i + 1 < n:
        while k < n and j <= i:
            natural_numbers[k] = 1
            j += 1
            k = i + j + 2 * i * j
        i += 1
        k = j = 0
    print(natural_numbers)

    for i in range(1, n):
        if natural_numbers[i] == 0:
            primes.append(2 * i + 1)
    return primes


print(gen_sundaram(n))







