from abc import ABC, abstractmethod

from .payment import Payment
from car_rental.bill import Bill

class PaymentStrategy(ABC):

    @abstractmethod
    def process_payment(self, bill: Bill, payment_amount: float) -> Payment:
        pass