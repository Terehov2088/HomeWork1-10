import random
("""Написать функцию для поиска разницы между максимальным и минимальным числом 
среди num_limit случайно сгенерированных чисел в указанном числовом диапазоне.
def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
 """)

def diff_min_max(num_limit, lower_bound, upper_bound):
    max_num = lower_bound
    min_num = upper_bound
    for i in range(num_limit):
        n = random.randint(lower_bound, upper_bound)
        if max_num < n or max_num == n:
            max_num = n
            print(max_num)
        if min_num > n or min_num == n:
            min_num = n
            print(min_num)
    delta_num = max_num - min_num

    return delta_num

result = diff_min_max(10, 1, 100)
print(result)
