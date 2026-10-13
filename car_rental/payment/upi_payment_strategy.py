
from datetime import datetime
from threading import Lock

from .payment import Payment
from .payment_mode import PaymentMode
from .payment_strategy import PaymentStrategy
from car_rental.bill import Bill

class UPIPaymentStrategy(PaymentStrategy):
    def __init__(self):
        self._id_lock: Lock = Lock()
        self._current_id: int = 9000

    def _get_and_increment_id(self) -> int:
        with self._id_lock:
            allocated_id = self._current_id
            self._current_id += 1
            return allocated_id

    def process_payment(self, bill: Bill, payment_amount: float) -> Payment:

        payment = Payment(
            payment_id = self._get_and_increment_id(),
            bill_id = bill.bill_id,
            amount_paid = payment_amount,
            payment_mode = PaymentMode.UPI,
            payment_date = datetime.now()
        )

        bill.bill_paid = True
        
        return payment
        