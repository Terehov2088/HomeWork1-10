from enum import Enum
class Game(Enum):
    ROCK = 0
    PAPPER = 1
    SCISSORS = 2

print(repr(Game.ROCK))
print(Game.ROCK.name)