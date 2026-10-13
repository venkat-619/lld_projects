from dataclasses import dataclass
from datetime import date

from .payment_mode import PaymentMode

@dataclass
class Payment:
    payment_id: int
    bill_id: int
    amount_paid: float
    payment_mode: PaymentMode
    payment_date: date
