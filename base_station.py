import random
import math
import numpy as np


class Generator:
    # parameters
    length = 5000
    x = 2000
    # min = 5
    # max = 50
    mean = 0
    standard_deviation = 4
    var_lambda = 0.1

    # function to assign values to object properties
    def __init__(self):
        self.power_bs1 = 0
        self.power_bs2 = 0
        self.speed = 0
        self.ttt_counter = 0
        self.actual_length = 0

    def rand_speed(self):
        # self.min = 5
        # self.max = 50
        # speed = [round(random.uniform(min, max), 2) for _ in range(1)]
        speed = np.random.randint(5, 50)
        return speed

    def rand_gaussian(self):
        g = np.random.randint(1, 25)
        s = (g - self.mean) / self.standard_deviation
        return s

    def rand_exp(self):
        k = np.random.randint(1, 25)
        tau = 1 - math.exp(-(1 / self.var_lambda) * k)
        # k = 50
        # tau = expon.cdf(x=50, scale=1/self.var_lambda)
        return tau

    def get_power_left(self, speed, time):
        self.actual_length = self.x + speed * time
        PBS1 = 4.56 - 22 * math.log10(self.actual_length) + self.rand_gaussian()
        return PBS1

    def get_power_right(self, device_id, speed, time):
        self.actual_length = self.length - (self.x + speed * time)
        if self.actual_length < self.x:
            print(f'User with id {device_id} has been removed from the system!')
            print('...')
            del device_id
            PBS2 = 0
        else:
            PBS2 = 4.56 - 22 * math.log10(self.actual_length) + self.rand_gaussian()
        return PBS2
