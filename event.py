from abc import ABC, abstractmethod
from system import Network
from base_station import Generator
from sortedcontainers import SortedList


class Event(ABC):

    time: int = 0                       # time of execution

    def __init__(self, time: int) -> None:
        super().__init__()
        self.time = time

    @abstractmethod
    def execute(self, network: Network, generator: Generator, event_list: SortedList):
        pass
