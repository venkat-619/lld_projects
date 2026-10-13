from typing import Dict

from ParkingLot.enums import VehicleType
from ParkingLot.entity import ParkingSpot
from ParkingLot.spot_managers import ParkingSpotManager

class ParkingLevel:

    def __init__(self, level_number: int, managers: Dict[VehicleType, ParkingSpotManager]):
        self._level_number = level_number
        self._managers = managers

    @property
    def level_number(self) -> int:
        return self._level_number

    def has_availability(self, vehicle_type: VehicleType) -> bool:
        manager = self._managers.get(vehicle_type, None)
        return (manager is not None and manager.has_free_spot())

    def park(self, vehicle_type: VehicleType) -> ParkingSpot:
        manager = self._managers.get(vehicle_type, None)
        if manager is None:
            raise ValueError(f"No parking manager for vehicle type: {vehicle_type}")
        return manager.park()

    def un_park(self, vehicle_type: VehicleType, spot: ParkingSpot) -> None:
        manager = self._managers.get(vehicle_type, None)

        if manager is not None:
            manager.un_park(spot)