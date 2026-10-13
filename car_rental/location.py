from dataclasses import dataclass

@dataclass
class Location:
    building_no: int
    area: str
    city: str
    state: str
    country: str
    pincode: int