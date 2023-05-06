from system import Network
from event import Event
from base_station import Generator
from sortedcontainers import SortedList


class ReportEvent(Event):
    device_id: int = None
    delta = 8

    def __init__(self, device_id: int, user_speed: int, time: int) -> None:
        Event.__init__(self, time=time)
        self.device_id = device_id
        self.user_speed = user_speed

    #def check_HO_conditional(self):
    # power condition: alpha i ttt
    # calling the power calculation function
    # if(Pt - Ps > alpha and t == ttt):
        # if the condition is met, we will switch the user

    def execute(self, network: Network, generator: Generator, event_list: SortedList):
        # TODO: Put the logic related with handover procedure here
        #
        # if user is still in the system plan new user report
        power_bs1 = round(generator.get_power_left(self.user_speed, self.time), 2)
        power_bs2 = round(generator.get_power_right(self.device_id, self.user_speed, self.time), 2)

        # power user after deleting with the system
        if power_bs2 == 0:
            power_bs1 = 0
        print(f'Received Power Report from User {self.device_id} '
              f'is equal PBS1: {power_bs1} dBm and PBS2: {power_bs2} dBm')
        event_list.add(ReportEvent(device_id=self.device_id, user_speed=self.user_speed, time=self.time + 20))

        # checking the radio link breakage
        if power_bs2 - power_bs1 < self.delta:
            del self.device_id


