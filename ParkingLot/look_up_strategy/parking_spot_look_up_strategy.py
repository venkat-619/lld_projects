from abc import ABC, abstractmethod
from typing import List

from ParkingLot.entity import ParkingSpot

class ParkingSpotLookUpStrategy(ABC):

    @abstractmethod
    def select_spot(self, spots: List[ParkingSpot]) -> ParkingSpot:
        pass
