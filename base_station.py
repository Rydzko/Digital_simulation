import random
import math
import numpy as np


class Generator:
    # parameters
    length = 5000
    min = 5
    max = 50
    mean = 0
    standard_deviation = 4
    var_lambda = 0.1

    # function to assign values to object properties
    def __init__(self):
        self.power_bs1 = 0
        self.power_bs2 = 0
        self.speed = 0
        self.ttt_counter = 0

    def rand_speed(self):
        #self.min = 5
        #self.max = 50
        #speed = [round(random.uniform(min, max), 2) for _ in range(1)]
        speed = np.random.randint(1, 25)
        return speed

    def rand_gaussian(self):
        x = random()
        u = (x - self.mean)/self.standard_deviation
        return u

    def rand_exp(self):
        k = random()
        return (1/self.var_lambda) * math.log2(k)

    def get_power(self, actual_length, length):
        P_b1 = 4.56 - 22*math.log10(actual_length) + Generator.rand_exp()
        P_b2 = 4.56 - 22*math.log10(length-actual_length) + Generator.rand_exp()
        return P_b1, P_b2