from base_station import *
import math

# user power report after t time in the system
#power_bs1 = 0                       #dBm
#power_bs2 = 0                       #dBm

# power variable
#alpha = 0

# t time
#t = 20*10 ^ (-3)                      #time
# Time to Trigger
#ttt = 0


class User:
    # function to assign values to object properties
    def __init__(self, power, speed, ttt_counter):
        self.power = power
        self.speed = speed
        self.ttt_counter = ttt_counter

    # power calculation
    #def speed(self):
    #    self.speed = Generator().rand_speed()
    def user(self):


    def power(self):
        self.power = Generator().get_power()

    def check_HO_conditional(self, power_t, power_s):
#warunek na moc: lambda i tto
        Pt - Ps > lambdaa

# call object
