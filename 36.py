import pprint
from vehicle.train import Train
from vehicle.airbus import Airbus


train1 = Train(60,20,100000 , 70, 20)
train1.set_color('Blue')
train1.pretty_print()



airbus1 = Airbus(
    speed=1000,
    old=10,
    price=30000000,
    tank_volume=20,
    fuel_consumption=1
)
airbus1.set_color('Green')
airbus1.pretty_print()