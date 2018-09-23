"""
Задача 36. Создать класс Транспортное средство и его потомков - классы Поезд и Самолет.
В родительском классе должно быть определено минимум 1 конструктор, 3 атрибута и 1 метод.
В классах-потомках должны быть добавлены минимум по 1 новому методу и по 1 новому атрибуту.
"""


class Vehicle():
    EXTRA_CHARGE = 4


    def __init__(self, speed, life_time, price):
        self.speed = speed
        self.price = price
        self.life_time = life_time
        self.color = ""


    def pretty_print(self):
        print('Speed, km/hour:', self.speed)
        print('Lifetime, year:', self.life_time)
        print('Price of vehicle, USD:', self.price)
        print('Revenue, USD:', self.revenue_for_year())
        print('Color:', self.color)


    def revenue_for_year(self):
        revenue_for_year = (self.price * self.EXTRA_CHARGE / self.life_time)
        return revenue_for_year

    def set_color(self, color):
        if not isinstance(color, str):
            print("Is invlid data!!!")
        else:
            self.color = color

    def get_color(self):
        return self.color




def main():
    if __name__ == '__main__':
        main()
