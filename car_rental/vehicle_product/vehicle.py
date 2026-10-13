
from .vehicle_type import VehcileType
from .vehicle_status import VehicleStatus

class Vehicle:
    def __init__(self, vehicle_id: int, vehicle_number: str, vehicle_type: VehcileType):
        self.vehicle_id = vehicle_id
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.daily_rental_cost: float = 0.0
        self.vehicle_status: VehicleStatus = VehicleStatus.AVAILABLE

    def set_daily_rental_cost(self, cost: float) -> None:
        self.daily_rental_cost = cost

    def set_status(self, status: VehicleStatus) -> None:
        self.vehicle_status = status