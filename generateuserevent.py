from event import Event
from reportevent import ReportEvent
from system import Network
from base_station import Generator
from sortedcontainers import SortedList
import numpy as np


class GenerateUserEvent(Event):

    def __init__(self, time: int) -> None:
        Event.__init__(self, time=time)

    def execute(self, network: Network, generator: Generator, event_list: SortedList):

        # add statistics
        id = network.generate_packet()
        speed = generator.rand_speed()
        print(f'Generated user with id {id} has a speed of {speed} m/s')
        print('---------------------')

        # generate new event
        time = np.random.randint(1, 25) + self.time
        #time = generator.rand_exp() + self.time
        event_list.add(GenerateUserEvent(time=time))

        # generate user report event
        event_list.add(ReportEvent(device_id=id, user_speed=speed, time=self.time + 20))
