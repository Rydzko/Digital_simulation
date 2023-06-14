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
    kM = 2147483647.0
    kA = 16807
    kQ = 127773
    kR = 2836
    users_served = []

    # function to assign values to object properties
    def __init__(self):
        self.power_bs1 = 0
        self.power_bs2 = 0
        self.speed = 0
        self.ttt_counter = 0
        self.actual_length = 0
        self.kM = 2147483647.0
        self.kA = 16807
        self.kQ = 127773
        self.kR = 2836
        self.kernel_ = 44

    def rand_kernel(self):
        h = int(self.kernel_/self.kQ)
        self.kernel_ = int(self.kA*(self.kernel_ - self.kQ*h) - self.kR*h)
        if self.kernel_ < 0:
            self.kernel_ = self.kernel_ + int(self.kM)
        return self.kernel_/self.kM

    def rand_speed(self):
        # speed = np.random.randint(5, 50)
        speed = int(np.random.uniform(5, 50, size=None))
        return speed

    def rand_gaussian(self):
        # g = np.random.randint(1, 25)
        # s = (g - self.mean) / self.standard_deviation
        s = int(np.random.normal(self.mean, self.standard_deviation, size=None))
        return s

    def rand_exp(self):
        # k = np.random.randint(1, 25)
        # tau = 1 - math.exp(-(1 / self.var_lambda) * k)
        # tau = (1/self.var_lambda)*math.exp(-(k/self.var_lambda))
        tau = int(np.random.exponential(1/self.var_lambda, size=None))
        return tau

    def get_power_left(self, speed, time):
        self.actual_length = self.x + speed * time
        PBS1 = 4.56 - 22 * math.log10(self.actual_length) + self.rand_gaussian()
        return PBS1

    def get_power_right(self, network: Network, device_id, speed, time):
        self.actual_length = self.length - (self.x + speed * time)
        if self.actual_length < self.x:
            if device_id in network.users_list:
                print(f'User with id {device_id} has been removed from the system!')
                print('...')
                if len(self.users_served) == 0:
                    self.users_served.append(1)
                else:
                    self.users_served.append(self.users_served[-1] + 1)
                # print(network.users_list)
                network.users_list.remove(device_id)
                del device_id
                print(network.users_list)
            PBS2 = 0
        else:
            PBS2 = 4.56 - 22 * math.log10(self.actual_length) + self.rand_gaussian()
        return PBS2
