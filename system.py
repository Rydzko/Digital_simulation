from main import *
from base_station import *

# length between basic stations
#l = 5000                            #meters

# amount of users
n = 1

# length x between first station and user appearing
#x = 2000                            #meters

# users appearing in the system - distributed random variable exponential with intensity λ
#tau = 0                             #time

# t time
t = 20*10 ^ (-3)                      #time

# case of breaking the radio link and removing the user from the system
#delta = 8                           #dB

class Network:
    # users queue
    #queue = []
    # users list
    #user_list = []

    def __init__(self, clock, user):
        self.user = user
        self.appear_time = clock
        self.delta = 8
        self.user_list = []
        self.queue = []
        self.tau = Generator.rand_exp()

    def create_user(self):
        # condition whether you need to add another user
        if (clock - self.appear_time) == self.tau:
            #appear_time = clock
            #create new user
            #Simulator.create_user()
            if self.user_list.count() > n:
                self.queue.append(self.user)
            else
                self.user_list.append(self.user)

    def user_power_report(self):


    # case when the user can leave the system
    def leave_system(self):
        #if user is matching with first station
        # if (P_b2 - P_b1) >= self.delta:
            self.user.delete()