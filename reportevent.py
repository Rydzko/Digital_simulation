from system import Network
from event import Event
from base_station import Generator
from sortedcontainers import SortedList


class ReportEvent(Event):
    network: Network
    generator: Generator
    event_list: SortedList

    device_id: int = None
    delta = 8
    alpha = 3
    ttt = 100
    ttt_counter = 0
    HO_counter = 0
    # dictionaries
    id_dict = {}

    def __init__(self, device_id: int, user_speed: int, time: int) -> None:
        Event.__init__(self, time=time)
        self.network = Network()
        self.generator = Generator()
        self.event_list = SortedList(key=lambda x: x.time)
        self.device_id = device_id
        self.user_speed = user_speed

    def execute(self, network: Network, generator: Generator, event_list: SortedList):
        if self.device_id in network.users_list:
            power_bs1 = round(generator.get_power_left(self.user_speed, self.time), 2)
            power_bs2 = round(generator.get_power_right(self.network, self.device_id, self.user_speed, self.time), 2)

        # TODO: Put the logic related with handover procedure here
        while self.id_dict.get(self.device_id) is not None:
            if power_bs1 - power_bs2 > self.alpha:
                self.ttt_counter = self.ttt_counter + 20
                self.id_dict[self.device_id] = self.ttt_counter
                if self.ttt_counter == self.ttt:
                    self.HO_counter = self.HO_counter + 1
                    self.ttt_counter = 0

        # power user after deleting with the system
        if self.device_id in network.users_list:
            if power_bs2 == 0:
                power_bs1 = 0
            print(f'Received Power Report from User {self.device_id} '
                  f'is equal PBS1: {power_bs1} dBm and PBS2: {power_bs2} dBm')
            event_list.add(ReportEvent(device_id=self.device_id, user_speed=self.user_speed, time=self.time + 20))
            # checking the radio link breakage
            if power_bs2 - power_bs1 < self.delta:
                print(f'User with id {self.device_id} has been removed from the system!')
                print('___')
                print(network.users_list)
                network.users_list.remove(self.device_id)
                del self.device_id
                print(network.users_list)
                print('@@@')