from dataclasses import dataclass
from typing import Optional
from .item import Item

@dataclass
class ItemShelf:
    code: int
    sold_out: bool
    item: Optional[Item] = None