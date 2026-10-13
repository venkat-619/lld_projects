
from .pricing_strategy import PricingStrategy
from ParkingLot.ticket import Ticket

class FixedPricingStrategy(PricingStrategy):

    def calculate(self, ticket: Ticket) -> float:
        return 100.0