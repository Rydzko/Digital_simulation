from system import Network
from generateuserevent import GenerateUserEvent
from reportevent import ReportEvent
from base_station import Generator
from sortedcontainers import SortedList
import os
import numpy as np


class MainLoop:

    numer_of_rands = 100000
    network: Network
    generator: Generator
    event_list: SortedList

    def __init__(self) -> None:
        self.network = Network()
        self.generator = Generator()
        self.event_list = SortedList(key=lambda x: x.time)

    def run(self, max_users):
        if os.stat('example.txt').st_size == 0:
            for i in range(0, self.numer_of_rands):
                with open('example.txt', 'a') as file:
                    file.write(f'{self.generator.rand_kernel()}\n')

        # MAIN LOOP
        time = 0
        correct_id = 0
        self.network.initialize()
        self.event_list.add(GenerateUserEvent(time=0))

        while correct_id < max_users:
            time = self.event_list[0].time
            print(f'Simulation time: {time} ms')
            event = self.event_list.pop(index=0)
            # id value can be equal None
            id = event.execute(self.network, self.generator, self.event_list)
            if id is not None:
                correct_id = id

            speed = self.generator.rand_speed()
            if (len(self.network.users_queue_list) != 0) and (self.network.user_counter > len(self.network.users_list)):
                self.network.users_list.append(self.network.users_queue_list[0])
                self.network.user = self.network.users_queue_list[0]
                self.network.users_queue_list.pop(0)
                print('After delete user with queue:')
                print(self.network.users_queue_list)
                print(f'Generated user with id {self.network.user} has a speed of {speed} m/s')
                print('----------------------')

                # number of users in the system for the final report
                if len(GenerateUserEvent.users_in_system) == 0:
                    GenerateUserEvent.users_in_system.append(1)
                else:
                    GenerateUserEvent.users_in_system.append(GenerateUserEvent.users_in_system[-1] + 1)

                # generate new event
                temp_time = time
                time = np.random.randint(1, 25) + time
                # time = self.generator.rand_exp()
                self.event_list.add(GenerateUserEvent(time=time))

                if self.network.user in self.network.users_list:
                    # generate user report event
                    self.event_list.add(ReportEvent(device_id=id, user_speed=speed, time=temp_time + 20))
