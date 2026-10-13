
from dataclasses import dataclass, field
from datetime import date

from .reservation_type import ReservationType
from .reservation_status import ReservationStatus

@dataclass
class Reservation:
    reservation_id: int
    vehicle_id: int
    user_id: int
    date_booked_from: date
    date_booked_to: date
    reservation_type: ReservationType
    reservation_status: ReservationStatus = field(default=ReservationStatus.SCHEDULED)