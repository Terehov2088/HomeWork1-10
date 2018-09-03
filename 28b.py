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


GREETING = '''
Enter the words you want to encrypt:
    \'q\' for end write: '''




def input_from_keyboard():
    list1 = []
    while True:
        input_data = input(GREETING)
        if input_data == 'q':
            break

        list1.append(input_data)
        continue
    return list1

str_to_encode = input_from_keyboard()
print(str_to_encode)


# str_to_encode = input("Введите слово для закодировки: ")


def encode(str_to_encode):
    password_sequence = string.ascii_lowercase + string.digits
    print(password_sequence)
    encode_word = []
    idx = 0
    el = 0
    for j in str_to_encode:
        for i in str_to_encode[el]:
            if ord("a") <= ord(i) <= ord("z") and ord(i) >= ord("v"):
                i = chr(ord(i) - 70)
                encode_word.insert(idx, i)
                idx = idx + 1
            elif ord("0") <= ord(i) <= ord("4"):
                i = chr(ord(i) + 5)
                encode_word.insert(idx, i)
                idx = idx + 1
            elif ord("5") <= ord(i) <= ord("9"):
                i = chr(ord(i) + 44)
                encode_word.insert(idx, i)
                idx = idx + 1
            elif ord("a") <= ord(i) <= ord("u"):
                i = chr(ord(i) + 5)
                encode_word.insert(idx, i)
                idx = idx + 1
            else:
                i = chr(ord(i))
                encode_word.insert(idx, i)
                idx = idx + 1
        el += 1
    encode_word = "".join(encode_word)
    return encode_word

print(encode(str_to_encode))


        # for j in str_to_encode[i]:
        #     if ord(j) >= ord("v"):
        #         j = chr(ord(j) - 21)
        #         print(j)
        #     else:
        #         j = chr(ord(j) + 5)
        #         print(j)
        # print(str_to_encode)





# password_sequence = string.ascii_lowercase
# print(type(password_sequence))
# print(password_sequence)

