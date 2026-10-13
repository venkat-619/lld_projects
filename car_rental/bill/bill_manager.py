
from typing import Dict, Optional
from threading import Lock

from .bill import Bill
from .billing_strategy import BillingStrategy
from car_rental.reservation import Reservation

class BillManager:
    def __init__(self, billing_strategy: BillingStrategy):
        self._billing_strategy = billing_strategy
        self._bills: Dict[int, Bill] = {}
        self._lock = Lock()

    def generate_bill(self, reservation: Reservation) -> Bill:
        bill = self._billing_strategy.generate_bill(reservation=reservation)

        with self._lock:
            self._bills[bill.bill_id] = bill

        return bill

    def get_bill(self, bill_id: int) -> Optional[Bill]:
        with self._lock:
            return self._bills.get(bill_id)

    def set_billing_strategy(self, billing_stratefy: BillingStrategy) -> None:
        self._billing_strategy = billing_stratefy