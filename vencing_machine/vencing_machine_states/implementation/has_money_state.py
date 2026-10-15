
from typing import List, TYPE_CHECKING

from vencing_machine.vencing_machine_states import State, Coin

if TYPE_CHECKING:
    from vencing_machine.context import VendingMachine

class HasMoneyState(State):
    def __init__(self):
        print("Currently Vending Machine is in HasMoneyState")

    def click_on_start_product_selection_button(self, vending_machine: "VendingMachine") -> None:
        # inline imports
        from .selection_state import SelectionState
        vending_machine.set_vending_machine_state(SelectionState())

    def insert_coin(self, vending_machine: "VendingMachine", coin: Coin) -> None:
        print(f"Accepted the coin")
        vending_machine.coin_list.append(coin)

    def refund_money(self, vending_machine: "VendingMachine") -> List[Coin]:
        print(f"Returned the fully amount back in coin dispenser tray")
        # inline imports
        from .idle_state import IdleState
        vending_machine.set_vending_machine_state(IdleState(vending_machine))
        return vending_machine.coin_list