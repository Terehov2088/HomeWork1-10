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
shyfr = int(input("Введите шифр: "))



def encode_word(str_to_encode, shyfr):
    def encode_symbol(char, len_password, shyfr):
        str_password_sequence = string.ascii_lowercase + string.digits
        idx = str_password_sequence.index(char)
        char = ((idx + shyfr) % len_password)
        return char


    str_password_sequence = string.ascii_lowercase + string.digits
    encode_word = ""

    for char in str_to_encode:
        if char in str_password_sequence:
            len_password = len(str_password_sequence)
            idx1 = encode_symbol(char, len_password, shyfr)
            char = str_password_sequence[idx1]
            encode_word += char
        else:
            encode_word = encode_word + char

    return encode_word


print(encode_word(str_to_encode, shyfr))
