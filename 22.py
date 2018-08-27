("""
Случайным образом программа выбирает целое число от 1 до 10 и предлагает пользователю его угадать. 
Пользователь вводит число, а программа проверяет его и, если пользователь не угадал, то говорит больше или меньше.
 После чего опять просит угадать. И так пока пользователь не угадает выбранное число.
""")

import random

GREETING = '''
Enter a number from 1 to 10
    \'q\' for exit: '''

def game_big_number():

    pc_choice = random.randint(0, 10)
    while True:
        input_data = input(GREETING)
        if input_data == 'q':
            break

        if not input_data.isnumeric():
            print('Invalid data')
            continue

        if not 0 <= int(input_data) <= 10:
            print('Invalid data')
            continue


        user_choice = int(input_data)

        print('PC choice: %s' % pc_choice)
        if pc_choice == user_choice:
            print('You is Winner')
            break
        else:
            if pc_choice > user_choice:
                print('You did not guess the number, you need a number more %d, try again' % user_choice)
            if pc_choice < user_choice:
                print('You did not guess the number, you need a number less %d, try again' % user_choice)

game_big_number()