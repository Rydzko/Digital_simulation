from event import Event
from reportevent import ReportEvent
from system import Network
from base_station import Generator
from sortedcontainers import SortedList
# from main_loop import MainLoop
import numpy as np


class GenerateUserEvent(Event):
    queue_id = 0
    temp_list = []
    users_in_system = []

    def __init__(self, time: int) -> None:
        Event.__init__(self, time=time)

    def execute(self, network: Network, generator: Generator, event_list: SortedList):

        # add statistics
        id = network.generate_packet()
        self.temp_list.append(id)
        speed = generator.rand_speed()

        # additional protection against generation of the same user
        if self.temp_list.count(id) == 1:
            print(f'Generated user with id {id} has a speed of {speed} m/s')
            print('++++++++++++++++++++++')
            self.users_in_system.append(id)

            if len(self.users_in_system) == 0:
                self.users_in_system.append(1)
            else:
                self.users_in_system.append(self.users_in_system[-1] + 1)
            # generate new event
            time = np.random.randint(1, 25) + self.time

            # this case has the problem of drawing different time!
            # time = generator.rand_exp()
            event_list.add(GenerateUserEvent(time=time))

        # print(network.users_list)
        # check if the user is on the list, it may have been removed from the system!
        if id in network.users_list and self.temp_list.count(id) == 1:
            # generate user report event
            event_list.add(ReportEvent(device_id=id, user_speed=speed, time=self.time + 20))

        return id
