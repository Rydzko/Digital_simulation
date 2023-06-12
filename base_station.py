import math
import numpy as np
from system import Network


class Generator:
    # parameters
    length = 5000
    x = 2000
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
        speed = np.random.randint(5, 50)
        return speed

    def rand_gaussian(self):
        g = np.random.randint(1, 25)
        s = (g - self.mean) / self.standard_deviation
        return s

    def rand_exp(self):
        k = np.random.randint(1, 25)
        tau = 1 - math.exp(-(1 / self.var_lambda) * k)
        return tau

    def get_power_left(self, speed, time):
        self.actual_length = self.x + speed * time
        PBS1 = 4.56 - 22 * math.log10(self.actual_length) + self.rand_gaussian()
        return PBS1

    def get_power_right(self, network: Network, device_id, speed, time):
        self.actual_length = self.length - (self.x + speed * time)
        if self.actual_length < self.x:
            print('LOLLL')
            print(device_id)
            if device_id in network.users_list:
                print(f'User with id {device_id} has been removed from the system!')
                print('...')
                print(network.users_list)
                network.users_list.remove(device_id)
                del device_id
                print(network.users_list)
                print('###')
            PBS2 = 0
        else:
            PBS2 = 4.56 - 22 * math.log10(self.actual_length) + self.rand_gaussian()
        return PBS2
