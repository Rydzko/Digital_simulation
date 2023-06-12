from event import Event
from reportevent import ReportEvent
from system import Network
from base_station import Generator
from sortedcontainers import SortedList
import numpy as np


class GenerateUserEvent(Event):
    queue_id = 0
    temp_list = []

    def __init__(self, time: int) -> None:
        Event.__init__(self, time=time)

    def execute(self, network: Network, generator: Generator, event_list: SortedList):

        # add statistics
        id = network.generate_packet()
        self.temp_list.append(id)
        # print(self.temp_list)
        # print('WRRR')
        speed = generator.rand_speed()
        speed_with_queue = generator.rand_speed()

        if self.temp_list.count(id) == 1:
            print(f'Generated user with id {id} has a speed of {speed} m/s')
            print('---------------------')
            # generate new event
            time = np.random.randint(1, 25) + self.time
            event_list.add(GenerateUserEvent(time=time))

        # if self.queue_id != id:
        print(id)
        print('OKEJ')
        # check if the user is on the list, it may have been removed from the system!
        if id in network.users_list:
            # generate user report event
            event_list.add(ReportEvent(device_id=id, user_speed=speed, time=self.time + 20))
            if len(network.users_queue_list) != 0 and network.user_counter >= len(network.users_list):
                network.users_list.append(network.users_queue_list[0])
                network.user = network.users_queue_list[0]
                network.users_queue_list.pop(0)
                print('After delete user with queue:')
                print(network.users_queue_list)
                print(f'Generated user with id {network.user} has a speed of {speed_with_queue} m/s')
                print('---------------------')
                # generate new event
                time = np.random.randint(1, 25) + self.time
                event_list.add(GenerateUserEvent(time=time))

        return id
