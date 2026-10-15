
from typing import TYPE_CHECKING

from vencing_machine.vencing_machine_states import State

if TYPE_CHECKING:
    from vencing_machine.context import VendingMachine, Item


class IdleState(State):
    def __init__(self, vending_machine: "VendingMachine" = None):
        print("Currently Vending Machine is in Idle State")
        if vending_machine is not None:
            vending_machine.coin_list = []

    def click_on_insert_coin_button(self, vending_machine: "VendingMachine") -> None:
        # inline imports
        from .has_money_state import HasMoneyState
        vending_machine.set_vending_machine_state(HasMoneyState())

    def update_inventory(self, vending_machine: "VendingMachine", item: "Item", code: int) -> None:
        vending_machine.inventory.add_item(item, code)