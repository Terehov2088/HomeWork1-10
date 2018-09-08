import random
import string
import math
("""По рзелульаттам илссеовадний одонго анлигйсокго унвиертисета, не иеемт занчнеия, в кокам пряокде рсапожолены бкувы в солве. 
Галвоне, чотбы преавя и пслоендяя бквуы блыи на мсете. 
Осатьлыне бкувы мгоут селдовтаь в плоонм бсепордяке, все-рвано ткест чтаитсея без побрелм. 
Пичрионй эгото ялвятеся то, что мы чиатем не кдаужю бкуву по отдльенотси, а все солво цликеом.

Напишите функцию, которая преобразует переданный ей текст способом, похожим на описанный выше. 
В качестве алгоритма перемешивания букв в слове используйте следующий:

Для каждого слова в тексте:
	1. Фиксируем первый и последний символы слова.
	2. Из оставшихся берём первые три символа, произвольно перемешиваем.
	3. Полученную тройку фиксируем, т.е. она уже не будет участвовать в дальнейшем перемешивании.
	4. Повторяем пункт 2, пока незафиксированные символы не кончатся.
	
	
def pemrtuate(text): # returns permuted text
""")


text = """Для енота полоскуна наиболее пригодны смешанные леса со старыми дуплистыми деревьями и наличием водоёмов или болот.
       Хвойных лесов, как и лесов, лишённых водоёмов, он избегает.
       На юге ареала водится на морском побережье. Еноты легко приспосабливаются к антропогенному ландшафту,
       селятся на окраинах полей, в садах, нередко в городах и пригородах.
       Жилища енот устраивает в дуплах.
       В крайнем случае использует наземные убежища — расщелины в скалах, норы барсуков; сам рыть норы не умеет.
       Ведёт сумеречно-ночной образ жизни; дневные часы проводит в логове.
       На промысел выходит с наступлением сумерек, обходя свой участок (радиусом до 1,5 км) в поисках пищи.
       Енот редко удаляется более чем на 1,5 километра от своего жилища.
       При этом участки отдельных особей часто перекрывают друг на друга, и, как результат,
       плотность енота в угодьях может быть довольно высоко"""


def pemrtuate(text):

    def permtuate_word(word):
        first = word[0]
        if word[-1] in string.punctuation:
            last = word[-2]
            middle = word[1:-2]
            punctuatinon = word[-1]
        else:
            last = word[-1]
            middle = word[1:-1]
            punctuatinon = " "
        old_i = 0
        new_word = first
        for i in range(math.ceil(len(middle) / 3)):
            sub_middle = list(middle[old_i:old_i + 3])
            random.shuffle(sub_middle)
            sub_middle = "".join(sub_middle)
            new_word = new_word + sub_middle
            old_i += 3
        new_word = new_word + last + punctuatinon
        return new_word


    word_list = [str(word.strip()) for word in text.split()]
    new_text = ""

    for word in word_list:
        if len(word) > 3:
            new_word = permtuate_word(word)
            new_text = new_text + " " + new_word
        else:
            new_text = new_text + " " + word


    return new_text

result = pemrtuate(text)

def line_translation(result):
    result = result + str(chr(22323))
    print(result)
    b = ' \n'
    idx = 0
    idx1 = 1
    result1 = ""
    for char in result:
        if char == result[-1]:
            c = result[idx1:idx1 + idx + 1]
            result1 = result1 + c
        else:
            if idx >= 80:
                if char == " ":
                    c = result[idx1:idx1 + idx]
                    idx1 = idx1 + idx
                    idx = 1
                    result1 = result1 + c + b
                else:
                    idx += 1
            else:
                idx += 1

    result1 = result1[0:-1]



    return result1

print(line_translation(result))









