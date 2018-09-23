import pprint
from .vehicle_options import Vehicle

class Train(Vehicle):
    TRAVEL_TIME = 10

    def __init__(self, speed, old, price, mass, long):
        super().__init__(speed, old, price)
        self.mass = mass
        self.long = long


    def travel_distance(self):
        travel_distance = self.speed * self.TRAVEL_TIME
        return travel_distance


    def pretty_print(self):
        super().pretty_print()
        print('Mass_train, t:', self.mass)
        print('Long_train, m:', self.long)
        print('Travel_distance, km:', self.travel_distance())
        print('=============')



