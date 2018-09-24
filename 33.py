""""
Задача 33. В файле https://github.com/dbradul/python_classes/blob/master/misc/titanic.csv
представлена реальная информация о пассажирах Титаника. Нас будут интересовать следующие колонки:
		Sex: пол пассажира
		Pclass: класс кабины
		Survived: выжил ли пассажир (1-да, 0-нет)

Определите сколько выжило пассажиров каждого пола и каждого класса кабины.
Соотнесите это с общим числом пассажиров каждого пола и класса кабины.
Таким образом, Вы определите как взаимосвязаны пол и класс кабины с выживаемостью.
"""

import string
import time
import csv
import pprint

def get_data_from_csv(filename):

    f = open(filename, "r")
    list_dicts = [row for row in csv.DictReader(f, delimiter=';')]
    f.close()

    return list_dicts


data_lst = get_data_from_csv(r'K:\text1.csv')
# for data in data_lst:
#     print('---------------------------')
#     for k, v in data.items():
#         print('\t', k, '->', v)

end = (len(data_lst)-1)
counter_male_all = 0
counter_female_all = 0
counter_male_surv = 0
counter_female_surv = 0

counter_pclass_all_1 = 0
counter_pclass_all_2 = 0
counter_pclass_all_3 = 0
counter_pclass_surv_1 = 0
counter_pclass_surv_2 = 0
counter_pclass_surv_3 = 0


for i in range(end, -1, -1):
    if (data_lst[i]['Survived']) == "0":
        if data_lst[i]['Sex'] == "male":
            counter_male_all +=1
        else:
            counter_female_all +=1

        if data_lst[i]['Pclass'] == "1":
            counter_pclass_all_1 +=1
        elif data_lst[i]['Pclass'] == "2":
            counter_pclass_all_2 +=1
        elif data_lst[i]['Pclass'] == "3":
            counter_pclass_all_3 +=1

    elif data_lst[i]['Survived'] == "1":
        if data_lst[i]['Sex'] == "male":
            counter_male_all +=1
            counter_male_surv += 1
        else:
            counter_female_all +=1
            counter_female_surv += 1

        if data_lst[i]['Pclass'] == "1":
            counter_pclass_all_1 +=1
            counter_pclass_surv_1 += 1
        elif data_lst[i]['Pclass'] == "2":
            counter_pclass_all_2 +=1
            counter_pclass_surv_2 += 1
        elif data_lst[i]['Pclass'] == "3":
            counter_pclass_all_3 +=1
            counter_pclass_surv_3 += 1

print('Всего мужчин на корабле: %d' % counter_male_all)
print('Всего выжило мужчин на корабле: %d' %counter_male_surv)
print('Всего женщин на корабле: %d' %counter_female_all)
print('Всего выжило женщин на корабле: %d' %counter_female_surv)
print('Всего пассажиров кают 1 класса: %d' %counter_pclass_all_1)
print('Всего выжило пассажиров кают 1 класса: %d' %counter_pclass_surv_1)
print('Всего пассажиров каюты 2 класса: %d' %counter_pclass_all_2)
print('Всего выжило пассажиров кают 2 класса: %d' %counter_pclass_surv_2)
print('Всего пассажиров каюты 3 класса: %d' %counter_pclass_all_3)
print('Всего выжило пассажиров кают 3 класса: %d' %counter_pclass_surv_3)

print('=================================')
ratio_of_survivors_male = (counter_male_surv / counter_male_all) * 100
ratio_of_survivors_female = (counter_female_surv / counter_female_all) * 100
ratio_of_survivors_1 = (counter_pclass_surv_1 / counter_pclass_all_1) * 100
ratio_of_survivors_2 = (counter_pclass_surv_2 / counter_pclass_all_2) * 100
ratio_of_survivors_3 = (counter_pclass_surv_3 / counter_pclass_all_3) * 100


print('Всего мужчин выжило %0.2f процента' % ratio_of_survivors_male)
print('Всего женщин выжило %0.2f процента' % ratio_of_survivors_female)
print('Всего пассажиров 1 класса выжило %0.2f процента' % ratio_of_survivors_1)
print('Всего пассажиров 2 класса выжило %0.2f процента' % ratio_of_survivors_2)
print('Всего пассажиров 3 класса выжило %0.2f процента' % ratio_of_survivors_3)
