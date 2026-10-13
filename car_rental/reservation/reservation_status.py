from enum import Enum

class ReservationStatus(Enum):
    SCHEDULED = "SCHEDULED"
    IN_USE = "IN_USE"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"