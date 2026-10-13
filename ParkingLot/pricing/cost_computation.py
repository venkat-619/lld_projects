
from .pricing_strategy import PricingStrategy
from ParkingLot.ticket import Ticket

class CostComputation:

    def __init__(self, pricing_strategy: PricingStrategy):
        self._pricing_strategy = pricing_strategy

    def compute(self, ticket: Ticket) -> float:
        return self._pricing_strategy.calculate(Ticket)
