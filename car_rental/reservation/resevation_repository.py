
from typing import Dict, Optional
from threading import Lock

from .reservation import Reservation

class ReservationRepository:

    def __init__(self):
        self._reservations: Dict[int, Reservation] = {}
        self._lock = Lock()

    def save(self, reservation: Reservation) -> None:
        with self._lock:
            self._reservations[reservation.reservation_id] = reservation

    def find_by_id(self, reservation_id: int) -> Optional[Reservation]:
        with self._lock:
            return self._reservations.get(reservation_id)

    def remove(self, reservation_id: int) -> None:
        with self._lock:
            if reservation_id in self._reservations:
                del self._reservations[reservation_id]

    def get_all(self) -> Dict[int, Reservation]:
        with self._lock:
            return dict(self._reservations)

