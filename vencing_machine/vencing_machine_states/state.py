
from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

from .coin import Coin

if TYPE_CHECKING:
    from vencing_machine.context import VendingMachine, Item
    

class State(ABC):

    def click_on_insert_coin_button(self, vending_machine: "VendingMachine") -> None:
        raise RuntimeError("Action not allowed in the current state.")

    def click_on_start_product_selection_button(self, vending_machine: "VendingMachine") -> None:
        raise RuntimeError("Action not allowed in the current state.")
    
    def insert_coin(self, vending_machine: "VendingMachine", coin: Coin) -> None:
        raise RuntimeError("Action not allowed in the current state.")

    def choose_product(self, vending_machine: "VendingMachine", code: int) -> None:
        raise RuntimeError("Action not allowed in the current state.")

    def get_change(self, return_change_money: int) -> int:
        return 0

    def dispense_product(self, vending_machine: "VendingMachine", code: int) -> "Item":
        raise RuntimeError("Action not allowed in the current state.")

    def refund_money(self, vending_machine: "VendingMachine") -> List[Coin]:
        raise RuntimeError("Action not allowed in the current state.")

    def update_inventory(self, vending_machine: "VendingMachine", item: "Item", code: int) -> None:
        raise RuntimeError("Action not allowed in the current state.")