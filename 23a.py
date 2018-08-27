import random

GREETING = '''
Enter data 
    0 - ROCK
    1 - PAPPER
    2 - SCISSORS
    \'q\' for exit: '''

from enum import Enum
class Game(Enum):
    ROCK = 0
    PAPPER = 1
    SCISSORS = 2


def code2text(code):
    if code == Game.ROCK.value:
        return 'ROCK'
    elif code == Game.PAPPER.value:
        return 'PAPPER'
    elif code == Game.SCISSORS.value:
        return 'SCISSORS'


def who_is_winner(pc_choice, user_choice):
    if pc_choice == Game.ROCK.value and user_choice == Game.SCISSORS.value:
        return False
    if pc_choice == Game.PAPPER.value and user_choice == Game.ROCK.value:
        return False
    if pc_choice == Game.SCISSORS.value and user_choice == Game.PAPPER.value:
        return False
    return True


def game():
    while True:
        input_data = input(GREETING)
        if input_data == 'q':
            break

        if not input_data.isnumeric():
            print('Invalid data')
            continue

        if not Game.ROCK.value <= int(input_data) <= Game.SCISSORS.value:
            print('Invalid data')
            continue

        pc_choice = random.randint(Game.ROCK.value, Game.SCISSORS.value)
        user_choice = int(input_data)

        print('PC choice: %s' % code2text(pc_choice))
        if pc_choice == user_choice:
            print('Tie')
        else:
            if who_is_winner(pc_choice, user_choice):
                print('User is winner: %s vs %s' %
                      (code2text(pc_choice),
                       code2text(user_choice)))
            else:
                print('PC is winner: %s vs %s' %
                      (code2text(pc_choice),
                       code2text(user_choice)))


game()