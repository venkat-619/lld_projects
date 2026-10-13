
from typing import List

from .parking_level import ParkingLevel
from ParkingLot.pricing import CostComputation
from ParkingLot.entity import Vehicle
from ParkingLot.ticket import Ticket

class ParkingBuilding:

    def __init__(self, levels: List[ParkingLevel], cost_computation: CostComputation):
        self._levels = levels
        self._cost_computation = cost_computation

    def allocate(self, vehicle: Vehicle) -> Ticket:

        v_type = vehicle.vehicle_type

        for level in self._levels:
            if level.has_availability(vehicle_type=v_type):
                spot = level.park(vehicle_type=v_type)
                if spot is not None: 
                    ticket = Ticket(vehicle=vehicle, level=level, spot=spot)
                    print(f"Parking allocated at Level : L{level.level_number} spot : {spot.spot_id}")
                    return ticket

        raise Exception("Parking Full...")

    def release(self, ticket: Ticket):
        ticket.level.un_park(
            ticket.vehicle.vehicle_type, 
            ticket.spot
        )

