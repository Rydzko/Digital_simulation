from system import Network
from generateuserevent import GenerateUserEvent
from base_station import Generator
from sortedcontainers import SortedList


class MainLoop:

    network: Network
    generator: Generator
    event_list: SortedList

    def __init__(self) -> None:
        self.network = Network()
        self.generator = Generator()
        self.event_list = SortedList(key=lambda x: x.time)

    def run(self, max_time):

        self.network.initialize()
        self.event_list.add(GenerateUserEvent(time=0))

        # MAIN LOOP
        time = 0
        while time < max_time:
            time = self.event_list[0].time
            print(f'Simulation time:{time} ms')
            event = self.event_list.pop(index=0)
            event.execute(self.network, self.generator, self.event_list)
