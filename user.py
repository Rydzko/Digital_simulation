from base_station import *
import math

# power variable
#alpha = 3                       #dB

# Time to Trigger
#ttt = 100*10 ^ (-3)             #ms

class User:
    # function to assign values to object properties
    def __init__(self, speed):
        #self.start_time = 0

        self.power = []
        self.speed = speed
        self.ttt = 100*10 ^ (-3)
        self.alpha = 3

    def power(self):
        self.power.append(Generator().get_power())

    def speed(self):
        self.speed = Generator().rand_speed()

    def check_HO_conditional(self):
    #power condition: alpha i ttt
    # wywolanie funkcji obliczajacej moc
        if(Pt - Ps > alpha and t == ttt):
            #jesli warunek bedzie spelniony to przelaczymy usera
