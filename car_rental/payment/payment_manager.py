
from typing import Dict, Optional
from threading import Lock

from car_rental.bill import Bill
from .payment import Payment
from .payment_strategy import PaymentStrategy

class PaymentManager:
    def __init__(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy
        self._payments: Dict[int, Payment] = {}
        self._lock: Lock = Lock()

    def make_payment(self, bill: Bill, payment_amount: float) -> Payment:
        payment = self._payment_strategy.process_payment(bill, payment_amount)

        with self._lock:
            self._payments[payment.payment_id] = payment
        
        return payment

    def get_payments_for_bill(self, bill_id: int) -> Optional[Payment]:
        with self._lock:
            return [ 
                payment for payment in self._payments.values()
                if bill_id == payment.bill_id
            ]

    def get_payment(self, payment_id: int) -> Optional[Payment]:
        with self._lock:
            return self._payments.get(payment_id)

    def set_payment_strategy(self, payment_strategy: PaymentStrategy) -> None:
        self._payment_strategy = payment_strategy