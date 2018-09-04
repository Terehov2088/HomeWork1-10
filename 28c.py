import string
import random
("""Создать программу, которая запрашивает у пользователя произвольную строку символов. 
Далее программа ее шифрует и выводит на экран в зашифрованном виде. 
Шифрование происходит путем замены каждого символа символом, который находится на 5 позиций правее в предопределенной таблице шифрования. 
Таблица шифрования задается программистом в виде одномерного списка символов латинского алфавита от a до z.
Если при выборе символа для шифровки таблица шифрования заканчивается, то циклически переходить к ее началу. 
Отсутствующие в таблице шифрования символы, записываются в результирующую строку без изменений. 
Регистр игнорируется.
	Таблица шифрования (a, b, c, d, ..., x, y, z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
	Например: Исходная строка, которую ввел пользователь: 'secret', 'office 365'
	Зашифрованная строка, которую выдала программа: 'xjhwjy', 'tkknhj 8ba'
	Примечание: т.н. таблица шифрования может быть представлена как строка или список.

def encode(str_to_encode): # returns enсoded string

""")

str_to_encode = input("Введите слово для закодировки: ")



def encode(str_to_encode):
    def symbol(i):
        str_password_sequence = string.ascii_lowercase + string.digits
        idx = 0
        for char in str_password_sequence:
            if i == char:
                i = ((idx + 5) % 36)
                return i
            else:
                idx += 1

        return i


    # list_to_encode = list(str_to_encode)
    # list_password_sequence = ([chr(i) for i in range(ord("a"), ord("z") + 1)] + [str(i) for i in range(0, 10)])
    str_password_sequence = string.ascii_lowercase + string.digits
    encode_word = ""

    for i in str_to_encode:
        if ord("a") <= ord(i) <= ord("z") or ord("0") <= ord(i) <= ord("9"):
            idx1 = symbol(i)
            i = str_password_sequence[idx1]
            encode_word += i
        else:
            encode_word = encode_word + i

    return encode_word


print(encode(str_to_encode))
