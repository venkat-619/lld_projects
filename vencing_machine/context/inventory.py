from typing import List, Optional

from .item_shelf import ItemShelf
from .item import Item

class Inventory:
    def __init__(self, item_count: int):
        self.inventory: List[Optional[ItemShelf]] = [None for _ in range(item_count)]
        self._initial_empty_inventory()

    def set_inventory(self, inventory: List[Optional[ItemShelf]]) -> None:
        self.inventory = inventory

    def _initial_empty_inventory(self):
        start_code = 101
        for i in range(len(self.inventory)):
            space = ItemShelf(code=start_code, sold_out=True)
            self.inventory[i] = space
            start_code += 1

    def add_item(self, item: Item, code: int) -> None:
        for item_shelf in self.inventory:
            if item_shelf.code == code:
                item_shelf.item = item
                item_shelf.sold_out = False
            else:
                raise Exception("Already Item is present, You can't add item")

    def get_item(self, code: int) -> Item:
        for item_shelf in self.inventory:
            if item_shelf.code == code:
                if not item_shelf.sold_out:
                    return item_shelf.item
                else:
                    raise Exception("Item already sold Out...")

        raise Exception("Item Not found in inventory")

    def update_sold_out_item(self, code:int) -> None:
        for item_shelf in self.inventory:
            if item_shelf.code == code:
                item_shelf.sold_out = True
                