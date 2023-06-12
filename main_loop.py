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

    def run(self, max_users):
        # MAIN LOOP
        time = 0
        correct_id = 0
        self.network.initialize()
        self.event_list.add(GenerateUserEvent(time=0))

        while correct_id < max_users:
            time = self.event_list[0].time
            print(f'Simulation time:{time} ms')
            event = self.event_list.pop(index=0)
            # id value can be equal None
            id = event.execute(self.network, self.generator, self.event_list)
            if id is not None:
                correct_id = id
