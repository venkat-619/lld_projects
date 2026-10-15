
from typing import List, TYPE_CHECKING

from vencing_machine.vencing_machine_states import State, Coin

if TYPE_CHECKING:
    from vencing_machine.context import VendingMachine

class SelectionState(State):
    def __init__(self):
        print("Currently Vending Machine is in SelectionState")

    def choose_product(self, vending_machine: "VendingMachine", code: int) -> None:
        item = vending_machine.inventory.get_item(code)

        paid_by_user = 0
        for coin in vending_machine.coin_list:
            paid_by_user += coin.value

        if paid_by_user < item.price:
            print(f"Insufficient Amount, Product you selected is for price : {item.price} and you paid : {paid_by_user}")
            self.refund_money(paid_by_user)
        else:
            if paid_by_user > item.price:
                self.get_change(paid_by_user - item.price)
                # inline imports
                from .dispense_state import DispenseState
                vending_machine.set_vending_machine_state(DispenseState(vending_machine, code))

    def get_change(self, return_change_money: int) -> int:
        print(f"Returned the change in coin dispense tray : {return_change_money}")
        return return_change_money

    def refund_money(self, vending_machine: "VendingMachine") -> List[Coin]:
        print(f"Returned the fully amount back in coin dispenser tray")
        # inline imports
        from .idle_state import IdleState
        vending_machine.set_vending_machine_state(IdleState(vending_machine))
        return vending_machine.coin_list