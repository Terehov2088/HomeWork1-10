("""
Для удобства проведения вступительных экзаменов всеx абитуриентов в MIT разбивают на группы в зависимости от первых букв их фамилии. 
Группы называются ‘A-I’, ‘J-P’, ‘Q-T’, ‘U-Z’. 
Название группы определяет в какую группу попадает абитуриент, в зависимости от первой буквы его/ее фамилии. 
Например, Will Smith попадает в группу ‘Q-T’, т.к. первая буква его фамилии попадает в диапазон букв от ‘Q‘ до ‘Т‘ (включительно!).
Абитуриент Jay Z попадает в группу ‘U-Z’ и т.д. Написать функцию, которая получает список имен студентов вида 
['Name1 Surname1', 'Name2 Surname2', 'Name3 Surname3', ...] и возвращает количество абитуриентов в группах, 
сформированных по их фамилиям, описанным выше образом.
     def group_by_surname(list_of_enrollees): # returns 4 ints
""")

list_of_enrollees = ['Roy Air', 'Donald Jakob', 'Kim Sell', 'Vladimir Xen', 'Vanya Chekov', 'Alehandro Ninderas']


def group_by_surname(list_of_enrollees):
    a_i = []
    j_p = []
    q_t = []
    u_z = []
    sum_a_i = 0
    sum_j_p = 0
    sum_q_t = 0
    sum_u_z = 0
    for elem in list_of_enrollees:
        elem1 = elem.split(' ')
        last_name = elem1[1]
        if ord("A") <= ord(last_name[0]) <= ord("I"):
            a_i.append(elem)
            sum_a_i += 1
        elif ord("J") <= ord(last_name[0]) <= ord("P"):
            j_p.append(elem)
            sum_j_p += 1
        elif ord("Q") <= ord(last_name[0]) <= ord("T"):
            q_t.append(elem)
            sum_q_t += 1
        elif ord("U") <= ord(last_name[0]) <= ord("Z"):
            u_z.append(elem)
            sum_u_z += 1
    return sum_a_i, sum_j_p, sum_q_t, sum_u_z


result1, result2, result3, result4 = group_by_surname(list_of_enrollees)

print('In the first group %d entrants.' % result1)
print('In the second group %d entrants.' % result2)
print('In the third group %d entrants.' % result3)
print('In the fourth group %d entrants.' % result4)




# lst = ['B', 'C', 'D', 'W', 'G', 'Z', 'X']
# sum = 0
# for elem in lst:
#     if ord("A") <= ord(elem) <= ord("I"):
#         sum += 1
#     print(sum)
#
# for i in range(ord('A'), ord('Z')):
#     print(i)

