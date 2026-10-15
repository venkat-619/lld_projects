from dataclasses import dataclass
from .item_type import ItemType

@dataclass
class Item:
    item_type: ItemType
    price: int