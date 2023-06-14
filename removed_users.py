import math
import numpy as np
from system import Network
# from event import Event
from generateuserevent import GenerateUserEvent
from base_station import Generator
from sortedcontainers import SortedList


class Remove:
    network: Network
    generator: Generator()
    event_list: SortedList

    delta = 10
    # function to assign values to object properties

    def __init__(self, time: int) -> None:
        # Event.__init__(self, time=time)
        self.time = None
        self.network = Network()
        self.generator = Generator()
        self.event_list = SortedList(key=lambda x: x.time)

    def removed_users(self, id, power_bs1, power_bs2):
        speed = self.generator.rand_speed()

        # checking the radio link breakage
        if power_bs2 - power_bs1 < self.delta:
            print(f'User with id {id} has been removed from the system!')
            print('___')
            print(self.network.users_list)
            self.network.users_list.remove(id)
            del id
            print(self.network.users_list)
            print('@@@')
            # GenerateUserEvent.execute(self.network, self.generator, self.event_list)

            if (len(self.network.users_queue_list) != 0) and (self.network.user_counter > len(self.network.users_list)):
                self.network.users_list.append(self.network.users_queue_list[0])
                self.network.user = self.network.users_queue_list[0]
                self.network.users_queue_list.pop(0)
                print('After delete user with queue:')
                print(self.network.users_queue_list)
                print(f'Generated user with id {self.network.user} has a speed of {speed} m/s')
                print('---------------------')
                # generate new event
                time = np.random.randint(1, 25) + self.time

                # this case has the problem of drawing different time!
                # time = generator.rand_exp()
                self.event_list.add(GenerateUserEvent(time=time))

    def deleted_users(self, id):
        speed = self.generator.rand_speed()

        print(f'User with id {id} has been removed from the system!')
        print('...')
        print(self.network.users_list)
        self.network.users_list.remove(id)
        del id
        print(self.network.users_list)
        print('###')

        if (len(self.network.users_queue_list) != 0) and (self.network.user_counter > len(self.network.users_list)):
            self.network.users_list.append(self.network.users_queue_list[0])
            self.network.user = self.network.users_queue_list[0]
            self.network.users_queue_list.pop(0)
            print('After delete user with queue:')
            print(self.network.users_queue_list)
            print(f'Generated user with id {self.network.user} has a speed of {speed} m/s')
            print('---------------------')
            # generate new event
            time = np.random.randint(1, 25) + self.time

            # this case has the problem of drawing different time!
            # time = generator.rand_exp()
            self.event_list.add(GenerateUserEvent(time=time))
