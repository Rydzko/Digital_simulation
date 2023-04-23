# length between basic stations
l = 5000                            #meters

# amount of users
n = 1

# users queue
queue = []

# length x between first station and user appearing
x = 2000                            #meters

# users appearing in the system - distributed random variable exponential with intensity λ
#tau = 0                             #time

# time simulation
clock = 0
# event management class
class Simulator:
    global clock

    # function to assign values to object properties
    def __init__(self):
        self.clock = 0

    def main_loop(self):


    #def add_user_to_sim(self):
    #warunek na sprawdzenie czy trzeba już dodac kolejnego usera
        #Simulator.create_user()