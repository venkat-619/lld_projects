from typing import List, Optional

from ParkingLot.entity import ParkingSpot
from .parking_spot_look_up_strategy import ParkingSpotLookUpStrategy

class RandomLookUpStrategy(ParkingSpotLookUpStrategy):

    def select_spot(self, spots: List[ParkingSpot]) -> Optional[ParkingSpot]:

        for spot in spots:
            if spot.is_free:
                return spot

        return None