import random
import math

# length between basic stations
l = 5000                            #meters

# amount of users
n = 1

# length x between first station and user appearing
#x = 2000                            #meters

class Generator:
    # parameters
    min = 5
    max = 50
    mean = 0
    standard_deviation = 4
    var_lambda = 0.1

    # function to assign values to object properties
    def __init__(self, power_bs1, power_bs2, speed, ttt_counter):
        self.power_bs1 = power_bs1
        self.power_bs2 = power_bs2
        self.speed = speed
        self.ttt_counter = ttt_counter

    def rand_speed(self):
        #self.min = 5
        #self.max = 50
        speed = [round(random.uniform(min, max), 2) for _ in range(1)]
        return speed

    def rand_gaussian(self):
        x = random()
        u = (x - self.mean)/self.standard_deviation
        return u

    def rand_exp(self):
        k = random()
        return (1/self.var_lambda) * math.log2(k)

    def get_power(self, d):
        P_b1 = 4.56 - 22*math.log10(d) + Generator.rand_exp()
        P_b2 = 4.56 - 22*math.log10(l-d) + Generator.rand_exp()
        return P_b1, P_b2