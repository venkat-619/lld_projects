
from abc import ABC, abstractmethod

from ParkingLot.ticket import Ticket

class PricingStrategy(ABC):

    @abstractmethod
    def calculate(self, ticket: Ticket) -> float:
        pass