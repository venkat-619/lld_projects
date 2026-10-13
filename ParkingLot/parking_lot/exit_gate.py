
from .parking_building import ParkingBuilding
from ParkingLot.ticket import Ticket
from ParkingLot.pricing import CostComputation
from ParkingLot.payment import Payment

class ExitGate:

    def __init__(self, cost_computation: CostComputation):
        self._cost_computation = cost_computation

    def complete_exit(self, building: ParkingBuilding, ticket: Ticket, payment: Payment) -> None:

        amount = self._calculate_price(ticket=Ticket)

        success = payment.pay(amount)

        if not success:
            raise Exception("Payment Failed. Exit Denied...")

        building.release(ticket=ticket)
        print(f"Exit Successfull. Gate Opened...")

    def _calculate_price(self, ticket: Ticket) -> float:
        return self._cost_computation.compute(ticket=Ticket)