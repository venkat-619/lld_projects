
from .parking_building import ParkingBuilding
from ParkingLot.ticket import Ticket
from ParkingLot.entity import Vehicle

class EntranceGate:

    def enter(self, building: ParkingBuilding, vehicle: Vehicle) -> Ticket:
        return building.allocate(vehicle=vehicle)