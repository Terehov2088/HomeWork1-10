("""
30. Написать функцию, возвращающую все простые числа от 1 до 100 в виде списка.

def gen_primes(): # returns list of ints
""")



n = int(input("Введите колличество чисел: "))


def gen_primes(n):
    natural_numbers = list(range(2, n + 1))
    for number in natural_numbers:
        if number != 0:
            for candidate in range(2 * number, n + 1, number):
                natural_numbers[candidate - 2] = 0
    primes = []
    for number in natural_numbers:
        if number != 0:
            primes.append(number)
    return primes

print(gen_primes(n))







