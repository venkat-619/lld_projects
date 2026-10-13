from abc import ABC, abstractmethod

from .bill import Bill
from car_rental.reservation import Reservation

class BillingStrategy(ABC):

    @abstractmethod
    def generate_bill(self, reservation: Reservation) -> Bill:
        pass