("""Каждому символу в таблице символов Unicode соответствует число. 
Написать функцию, которая рассчитывает сумму чисел, которые соответствуют символам, стоящим между двумя заданными включительно. 
Например, в функцию передаются символы ‘x’ и ‘z’. Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’. 
		def sum_symbol_codes(first, last): # returns int
 """)






def sum_symbol_codes(first, last):
    sum_char = 0
    for i in range(ord(first), ord(last) + 1):
        sum_char += i
    return sum_char

sum = sum_symbol_codes(input('Введите символ: '), input('Введите символ: '))
print(sum)



