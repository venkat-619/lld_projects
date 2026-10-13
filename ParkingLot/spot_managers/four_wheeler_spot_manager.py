from typing import List

from .parking_spot_manager import ParkingSpotManager
from ParkingLot.entity import ParkingSpot
from ParkingLot.look_up_strategy import ParkingSpotLookUpStrategy

class FourWheelerSpotManager(ParkingSpotManager):

    def __init__(self, spots: List[ParkingSpot], strategy: ParkingSpotLookUpStrategy):
        super().__init__(spots, strategy)