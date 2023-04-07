# length between basic stations
l = 5000                            #meters

# amount of users
n = 20

# users queue
queue = []

# length x between first station and user appearing
x = 2000                            #meters

# users appearing in the system - distributed random variable exponential with intensity λ
tau = 0                             #time
# user speed in system - random variable with uniform distribution on the interval [5, 50]
v = 0
# Gaussian random variable with mean zero and standard deviation equal to 4dB
s = 0                               #dB

# case when the user can leave the system


# user power report after t time in the system
#power_bs1 = 0                       #dBm
#power_bs2 = 0                       #dBm

# power variable
#alpha = 0

# t time
t = 20*10 ^ (-3)                      #time
# Time to Trigger
ttt = 0

# case of breaking the radio link and removing the user from the system
delta = 8                           #dB

# bedzie zarzadzac zdarzeniami
class Simulator:
    #d = 5000
    #d_user = 2000
    #def __init__(self, power):
    #    self.power = power
    #    seld.speed = speed

    #def create_user(self):
#warunek na sprawdzenie czy trzeba już dodac kolejnego usera

        #Simulator.create_user()