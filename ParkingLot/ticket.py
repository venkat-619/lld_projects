from dataclasses import dataclass, field
from datetime import datetime

from ParkingLot.entity import ParkingSpot, Vehicle
from ParkingLot.parking_lot import ParkingLevel

# A @dataclass is a built-in decorator that automatically writes all your boilerplate code for you.
# If a class is primarily built to store data and pass it around 
# By adding (frozen=True) to a dataclass, Python makes the entire object read-only

@dataclass(frozen=True)
class Ticket:
    vehicle: Vehicle
    level: ParkingLevel
    spot : ParkingSpot

    # if you want an attribute to default to a dynamic value that changes every time a new object is created
    # (like datetime.now() for a Ticket)
    # This is also strictly required if your default value is an empty list list or dictionary dict, 
    # using default_factory=list.
    entry_time: datetime = field(default_factory= datetime.now)
