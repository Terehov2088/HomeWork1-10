"""
31. В программе phone_book (https://github.com/dbradul/python/blob/master/phone_book.py) реализовать следующие функции:
find_entry_age_phonebook 		# найти все записи с указанным возрастом
print_phonebook_by_age		# распечатать все записи отсортированные по возрасту
delete_entry_name_phonebook	# удалить все записи с указанным именем
print_avr_age				# распечатать средний возраст всех абонентов
increase_age				# увеличить возраст всем абонентам на заданное пользователем кол-во лет
<ваша_функция>				# добавить любую функцию, манипулирующую записями (печать, добавление, удаление) в телефонной книге на ваше усмотрение.
добавить поддержку еще одного поля (например, скайп, адрес, день рождения) и сделайте по нему поиск и печать. Т.е. добавить функцию для поиска и обновить существующую функцию печати.

	При выполнении обратите внимание на обработку ошибок. Например, если при удалении записи с заданным именем нет, то вывести сообщение “Not found!”.
"""

import pickle
import pprint


running = True

#------------------------------------------------------------------------------
phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number":"+380501234567", "skype": "Petruchcho"},
              {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number":"+380507654321", "skype": "Ivanello"},
             ]


#------------------------------------------------------------------------------
def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])
    print ("| Phone:   %20s |" % entry["phone_number"])
    print ("| Skype:   %20s |" % entry["skype"])
    print ()


#------------------------------------------------------------------------------
def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
def add_entry_phonebook():
    surname = input("    Enter surname: ")
    name    = input("    Enter name: ")
    age     = int(input("    Enter age: "))
    phone_number   = input("    Enter phone num.: ")
    skype = input("    Enter skype.: ")

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    entry["skype"] = skype
    phone_book.append(entry)


#------------------------------------------------------------------------------
def printError(message):
    print ("ERROR: %s" % message)


#------------------------------------------------------------------------------
def printInfo(message):
    print ("INFO: %s" % message)


#------------------------------------------------------------------------------
def find_entry_name_phonebook():
    name = str(input("    Enter name: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def find_entry_age_phonebook():
    age = int(input("    Enter age: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
# def delete_entry_name_phonebook():
#     name = str(input("    Enter name: "))
#     end = True
#     while end:
#         found = False
#         idx = 0
#         for entry in phone_book:
#             if entry["name"] == name:
#                 del phone_book[idx]
#                 print_phonebook()
#                 found = True
#             else:
#                 idx += 1
#
#         if not found:
#             printError("Not found!!")
#             end = False


# def delete_entry_name_phonebook():
#     name = str(input("    Enter name: "))
#     found = False
#     idx = 0
#     a = len(phone_book)
#
#     for i in range(a):
#         print(phone_book[i])
#         if phone_book[i]["name"] == name:
#             # print(phone_book.index(entry))
#             # del phone_book[idx]
#             a = a -1
#             print_phonebook()
#             found = True
#         else:
#             idx += 1
#
#     if not found:
#         printError("Not found!!")

# def delete_entry_name_phonebook():
#     name = str(input("    Enter name: "))
#     found = False
#     idx = 0
#     a = (len(phone_book)-1)
#     while a > 0:
#         if phone_book[idx]["name"] == name:
#             del phone_book[idx]
#             a = a - 1
#         else:
#             a = a - 1
#             idx = idx + 1
#     if not found:
#         print("All records deleted!!")

def delete_entry_name_phonebook():
    name = str(input("    Enter name: "))
    found = False
    # idx = 0
    idx = (len(phone_book)-1)
    for i in range(idx, 0, -1):
        print(phone_book[i])
        print(phone_book[i]["name"])
        if phone_book[i]["name"] == name:
            del phone_book[i]

    if not found:
        print("All records deleted!!")



#------------------------------------------------------------------------------
def find_entry_skype():
    skype = str(input("    Enter skype: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["skype"] == skype:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))


#------------------------------------------------------------------------------
def print_phonebook_by_age():
    phone_book.sort(key=lambda elem: elem['age'], reverse=True)
    pprint.pprint(phone_book)


#------------------------------------------------------------------------------
def increase_age():
    inc_age = int(input("    Enter increase age: "))
    for entry in phone_book:
        if 'age' in entry:
            entry['age'] += inc_age
        else:
            employee['age'] = None
    print_phonebook()


#------------------------------------------------------------------------------
def avr_age_of_all_persons():
    avr_age = 0
    idx = 1
    for entry in phone_book:
        avr_age = avr_age + entry['age']/idx
        idx +=1

    print("Средний возраст: %.2f " % avr_age)

# ------------------------------------------------------------------------------
def sort_for_age():
    phone_book.sort(key=lambda elem: elem['age'], reverse=False)
    print_phonebook()


#------------------------------------------------------------------------------
def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


#------------------------------------------------------------------------------
def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


#------------------------------------------------------------------------------
def exit():
      global running
      running = False


#------------------------------------------------------------------------------
def print_prompt():
      print()
      print()
      print()
      print("~ Welcome to phonebook ~")
      print("Select one of actions below:")
      print("     1 - Print phonebook entries")
      print("     2 - Print phonebook entries (by age)")
      print("     3 - Add new entry")
      print("     4 - Find entry by name")
      print("     5 - Find entry by age")
      print("     6 - Delete entry by name")
      print("     7 - The number of entries in the phonebook")
      print("     8 - Avr. age of all persons")
      print("     9 - Increase age by num. of years")
      print("     10 - Sort for age")
      print("     11 - Find entry by skype")
      print("-----------------------------")
      print("     s - Save to file")
      print("     l - Load from file")
      print("     0 - Exit")
      print()


#------------------------------------------------------------------------------
def main():

    while running:
        try:

            menu = {
                  '1':  print_phonebook,
                  '2':  print_phonebook_by_age,
                  '3':  add_entry_phonebook,
                  '4':  find_entry_name_phonebook,
                  '5':  find_entry_age_phonebook,
                  '6':  delete_entry_name_phonebook,
                  '7':  count_all_entries_in_phonebook,
                  '8':  avr_age_of_all_persons,
                  '9':  increase_age,
                  '10': sort_for_age,
                  '11': find_entry_skype,

                  '0':  exit,
                  's':  save_to_file,
                  'l':  load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()