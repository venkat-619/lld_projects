
from ParkingLot.entity import Vehicle
from ParkingLot.ticket import Ticket
from ParkingLot.payment import Payment
from .parking_building import ParkingBuilding
from .entrance_gate import EntranceGate
from .exit_gate import ExitGate

class ParkingLot:
    def __init__(self, building: ParkingBuilding, entrace_gate: EntranceGate, exit_gate: ExitGate):
        self._building = building
        self._entrance_gate = entrace_gate
        self._exit_gate = exit_gate

    def vehicle_arrives(self, vehicle: Vehicle) -> Ticket:
        return self._entrance_gate.enter(building=self._building, vehicle=vehicle)

    def vehicle_exits(self, ticket: Ticket, payment: Payment) -> None:
        self._exit_gate.complete_exit(building=self._building, ticket=ticket, payment=payment)