
from typing import TYPE_CHECKING

from vencing_machine.vencing_machine_states import State

if TYPE_CHECKING:
    from vencing_machine.context import VendingMachine, Item

class DispenseState(State):
    def __init__(self, vending_machine: "VendingMachine", code: int):
        print("Currently Vending Machine is in DispenseState")
        self.dispense_product(vending_machine, code)

    def dispense_product(self, vending_machine: "VendingMachine", code: int) -> "Item":
        print(f"Product has been dispatched...")
        item = vending_machine.inventory.get_item(code)
        vending_machine.inventory.update_sold_out_item(code)
        # inline imports
        from .idle_state import IdleState
        vending_machine.set_vending_machine_state(IdleState(vending_machine))
        return item