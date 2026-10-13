
from threading import Lock

from .bill import Bill
from .billing_strategy import BillingStrategy
from car_rental.vehicle_product import VehicleInventoryManager

class DailyBillingStrategy(BillingStrategy):
    def __init__(self, vehicle_inventory: VehicleInventoryManager):
        self.vehicle_inventory = vehicle_inventory
        self._id_lock: Lock = Lock()
        self._current_id: int = 5000

    def _get_and_increment_id(self) -> int:
        with self._id_lock:
            allocated_id = self._current_id
            self._current_id += 1
            return allocated_id

    def generate_bill(self, reservation) -> Bill:

        days = (reservation.date_booked_to - reservation.date_booked_from).days + 1
        vehicle = self.vehicle_inventory.get_vehicle(reservation.vehicle_id)

        if vehicle is None:
            raise ValueError(f"Vehicle with ID {reservation.vehicle_id} not found in inventory...")

        rate = vehicle.daily_rental_cost

        total_cost = days * rate

        return Bill(
            bill_id= self._get_and_increment_id(),
            reservation_id=reservation.reservation_id,
            total_bill_amount=total_cost
        )
