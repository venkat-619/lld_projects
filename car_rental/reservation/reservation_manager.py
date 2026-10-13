
from typing import Optional, TYPE_CHECKING
from threading import Lock
from datetime import date

from .reservation import Reservation
from .reservation_type import ReservationType
from .reservation_status import ReservationStatus
from .resevation_repository import ReservationRepository
from car_rental.user import User

if TYPE_CHECKING:
    from car_rental.vehicle_product import VehicleInventoryManager

class ReservationManager:
    def __init__(self, inventory: "VehicleInventoryManager"):
        self._inventory = inventory
        self._reservation_repository: ReservationRepository = ReservationRepository()
        self._inventory.set_reservation_repository(self._reservation_repository)

        self._lock = Lock()
        self._current_id: int = 2000

    def _get_increment_id(self) -> int:
        with self._lock:
            allocated_id = self._current_id
            self._current_id += 1
            return allocated_id

    # get reservation
    def find_by_id(self, reservation_id) -> Optional[Reservation]:
        return self._reservation_repository.find_by_id(reservation_id=reservation_id)

    def create_reservation(
        self, 
        vehicle_id: int,  
        user: User, 
        from_date: date,
        to_date: date,
        type_enum: ReservationType
    ) -> Reservation:
        reservation_id = self._get_increment_id()
        reserved = self._inventory.reserve(vehicle_id, reservation_id, from_date, to_date)

        if not reserved:
            raise Exception(f"Vehicle not avaiable for selected dates")

        reservation = Reservation(
            reservation_id=reservation_id,
            vehicle_id=vehicle_id,
            user_id=...,
            date_booked_from= from_date,
            date_booked_to= to_date,
            reservation_type= type_enum
        )

        self._reservation_repository.save(reservation=reservation)
        return reservation

    def cancel_reservation(self, reservation_id: int) -> None:
        reservation = self._reservation_repository.find_by_id(reservation_id)
        if reservation is None:
            raise Exception("Reservation Not Found...")
        
        reservation.reservation_status = ReservationStatus.CANCELLED
        self._inventory.release(reservation.vehicle_id, reservation.reservation_id)
        self._reservation_repository.remove(reservation_id)

    def start_trip(self, reservation_id: int) -> None:
        reservation = self._reservation_repository.find_by_id(reservation_id)
        if reservation is None:
            raise Exception("Reservation Not Found...")
        reservation.reservation_status = ReservationStatus.IN_USE

    def submit_vehicle(self, reservation_id: int) -> None:
        reservation = self._reservation_repository.find_by_id(reservation_id)
        if reservation is None:
            raise Exception("Reservation Not Found...")
        reservation.reservation_status = ReservationStatus.COMPLETED
        self._inventory.release(reservation.vehicle_id, reservation.reservation_id)

    def remove(self, reservation_id: int) -> None:
        self._reservation_repository.remove(reservation_id)