
from typing import List

from .inventory import Inventory
from vencing_machine.vencing_machine_states import State, Coin
from vencing_machine.vencing_machine_states.implementation import IdleState

class VendingMachine:
    def __init__(self):
        self.inventory: Inventory = Inventory(10)
        self.vending_machine_state: State = IdleState(self)
        self.coin_list: List[Coin] = []

    def set_vending_machine_state(self, vending_machine_state: State):
        self.vending_machine_state = vending_machine_state