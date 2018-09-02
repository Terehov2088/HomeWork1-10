("""Напечатать таблицу Пифагора заданной конфигурации.
     def print_mult_table(n, m): # prints multiplication table n x m
 """)

def print_mult_table(n, m):
    formatter = '%%%dd' % (len(str(n*m))+1)
    for i in range(1, n+1):
        for j in range(1, m+1):
            print(formatter % (i*j), end='')
            #print(i * j, end='\t')
        print()

print(print_mult_table(3, 3))