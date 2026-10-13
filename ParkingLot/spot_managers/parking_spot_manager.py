
from abc import ABC
from typing import List, Optional
from threading import RLock

from ParkingLot.entity import ParkingSpot
from ParkingLot.look_up_strategy import ParkingSpotLookUpStrategy

class ParkingSpotManager(ABC):

    def __init__(self, spots: List[ParkingSpot], strategy: ParkingSpotLookUpStrategy):
        self._spots = spots
        self._strategy = strategy
        self._lock: RLock = RLock()

    def park(self) -> Optional[ParkingSpot]:

        with self._lock:
            spot = self._strategy.select_spot(self._spots)

            if spot is None:
                return None

            spot.occupy_spot()
            return spot

    def un_park(self, spot: ParkingSpot) -> None:
        with self._lock:
            spot.release_spot()

    def has_free_spot(self) -> bool:
        with self._lock:
            return any(spot.is_free for spot in self._spots)