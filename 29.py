import string
import random
("""Создать генератор паролей, который будет генерировать случайные неповторяющиеся пароли по следующим правилам:
Пароль состоит из 8 символов
В пароле допускаются только латинские большие и маленькие буквы, цифры и символ подчеркивания
Пароль обязательно должен содержать Большие и маленькие буквы и цифры

def gen_password(): # returns string
 """)


# password = string.ascii_lowercase + string.digits + string.ascii_uppercase
# number = (''.join([random.choice(password) for i in range(8)]))



def gen_password():
    end = True
    while end == True:
        password = "".join([chr(i) for i in range(ord("a"), ord("z") + 1)] + [chr(i) for i in range(ord("A"), ord("Z") + 1)] + [str(i) for i in range(0, 10)])
        number = (''.join([random.choice(password) for i in range(8)]))
        idx1 = 0
        idx2 = 0
        idx3 = 0
        for el in number:
            if ord("a") <= ord(el) <= ord("z"):
                idx1 += 1
            elif ord("A") <= ord(el) <= ord("Z"):
                idx2 += 1
            elif ord("0") <= ord(el) <= ord("9"):
                idx3 += 1
        if idx1 == 0 or idx2 == 0 or idx3 == 0:
            end = True
        else:
            end = False
    return number

gen_password()
print(gen_password())
