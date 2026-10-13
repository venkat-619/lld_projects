from dataclasses import dataclass, field

@dataclass
class Bill:
    bill_id: int
    reservation_id: int
    total_bill_amount: float
    bill_paid: bool = field(default=False)