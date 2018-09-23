import pprint
from .vehicle_options import Vehicle

class Airbus(Vehicle):
    ONE_THOUSAND_KILOMETERS = 1000

    def __init__(self, speed, old, price, tank_volume, fuel_consumption):
        super().__init__(speed, old, price)
        self.tank_volume = tank_volume
        self.fuel_consumption = fuel_consumption

    def distance_flight(self):
        distance_flight = (self.tank_volume / self.fuel_consumption) * self.ONE_THOUSAND_KILOMETERS
        return distance_flight



    def pretty_print(self):
        super().pretty_print()
        print('Tank volume, t:', self.tank_volume)
        print('Distance of flight, km:', self.distance_flight())
        print('=============')

