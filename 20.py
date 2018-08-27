import random
import math
("""Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел среди num_limit случайно сгенерированных 
чисел в указанном числовом диапазоне. 
Т.е. от суммы четных чисел вычесть сумму нечетных чисел.
		def diff_even_odd(num_limit, lower_bound, upper_bound): # returns int
 """)

def diff_even_odd(num_limit, lower_bound, upper_bound):
    sum_odd = 0 # нечетный
    sum_even = 0 # четный

    for i in range(num_limit):
        n = random.randint(lower_bound, upper_bound)
        if (n % 2) == 0:
            sum_even +=n
        else:
            sum_odd +=n
    delta_sum = math.fabs(sum_odd - sum_even)
    return delta_sum


difference_sum = diff_even_odd(10, -100, 100)
print('Difference between the sum of even and odd numbers: %d' % difference_sum)