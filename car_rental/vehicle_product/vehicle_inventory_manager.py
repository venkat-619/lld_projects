from collections import defaultdict
from typing import Dict, List, Optional
from threading import Lock
from datetime import date

from .vehicle import Vehicle
from .vehicle_status import VehicleStatus
from .vehicle_type import VehcileType
from .date_interval import DateInterval
from car_rental.reservation import ReservationRepository

class VehicleInventoryManager:
    def __init__(self):
        self._vehicles: Dict[int, Vehicle] = {}
        self._vehicle_booking_ids: Dict[int, List[int]] = defaultdict(list)
        self._global_lock: Lock = Lock()
        self._vehicle_locks: Dict[int, Lock] = {}
        self._reservation_repository: Optional[ReservationRepository] = None

    def add_vechile(self, vehicle: Vehicle)-> None:
        self._vehicles[vehicle.vehicle_id] = vehicle

    def get_vehicle(self, vehicle_id: int)-> Optional[Vehicle]:
        return self._vehicles.get(vehicle_id)

    def set_reservation_repository(self, repository: ReservationRepository) -> None:
        self._reservation_repository = repository

    def _lock_for_vehicle(self, vehcile_id: int)-> Lock:
        with self._global_lock:
            if vehcile_id not in self._vehicle_locks:
                self._vehicle_locks[vehcile_id] = Lock()
            return self._vehicle_locks[vehcile_id]

    def is_available(self, vehicle_id: int, from_date: date, to_date: date) -> bool:

        vehicle = self._vehicles.get(vehicle_id)

        if vehicle is None:
            return False

        if vehicle.vehicle_status == VehicleStatus.MAINTAINANCE:
            return False

        requested = DateInterval(from_date = from_date, to_date = to_date)
        reservation_ids = self._vehicle_booking_ids.get(vehicle_id)

        if not reservation_ids:
            return True

        for reservation_id in reservation_ids:
            reservation = self._reservation_repository.find_by_id(reservation_id)
            if reservation is not None:
                booked_interval = DateInterval(from_date=reservation.date_booked_from, to_date=reservation.date_booked_to)
                if booked_interval.overlaps(requested):
                    return False

        return True

    def reserve(self, vehicle_id: int, reservation_id: int, from_date: date, to_date: date) -> bool:
        lock = self._lock_for_vehicle(vehcile_id=vehicle_id)
        with lock:
            if not self.is_available(vehicle_id, from_date, to_date):
                return False

            self._vehicle_booking_ids[vehicle_id].append(reservation_id)
            self._vehicles[vehicle_id].set_status(VehicleStatus.BOOKED)
            return True

    def release(self, vehicle_id: int, reservation_id: int) -> None:
        lock = self._lock_for_vehicle(vehcile_id=vehicle_id)
        with lock:

            ids = self._vehicle_booking_ids.get(vehicle_id)
            if ids and reservation_id in ids:
                ids.remove(reservation_id)

            still_booked = self._vehicle_booking_ids.get(vehicle_id)
            if not still_booked:
                self._vehicles[vehicle_id].set_status(VehicleStatus.AVAILABLE)

    def get_available_vehicles(self, vehicle_type: VehcileType, from_date: date, to_date: date) -> List[Vehicle]:

        return [
            vehicle for vehicle in self._vehicles.values()
            if vehicle.vehicle_type == vehicle_type and self.is_available(vehicle.vehicle_id, from_date, to_date)
        ]

    