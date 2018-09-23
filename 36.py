import pprint
from vehicle.train import Train
from vehicle.airbus import Airbus


train1 = Train(60,20,100000 , 70, 20)
train1.set_color('Blue')
train1.pretty_print()



airbus1 = Airbus(1000,10,30000000 , 20, 1)
airbus1.set_color('Green')
airbus1.pretty_print()