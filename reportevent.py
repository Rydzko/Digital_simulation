from system import Network
from event import Event
from base_station import Generator
from sortedcontainers import SortedList


class ReportEvent(Event):
    device_id: int = None

    def __init__(self, device_id: int, time: int) -> None:
        Event.__init__(self, time=time)
        self.device_id = device_id

    #def check_HO_conditional(self):
    # power condition: alpha i ttt
    # calling the power calculation function
    # if(Pt - Ps > alpha and t == ttt):
        # if the condition is met, we will switch the user

    def execute(self, network: Network, generator: Generator, event_list: SortedList):
        # TODO: Put the logic related with handover procedure here
        #
        # if user is still in the system plan new user report
        print(f'Received Power Report from User {self.device_id}')
        event_list.add(ReportEvent(device_id=self.device_id, time=self.time + 20))
        # otherwise remove user

#    def leave_system(self):
    # if user is matching with first station
    # if (P_b2 - P_b1) >= self.delta:
#            self.user.delete()


