
from vencing_machine.context import VendingMachine, Item, ItemType
from vencing_machine.vencing_machine_states import Coin

def fill_inventory(vending_machine: VendingMachine) -> None:
    slots = vending_machine.inventory.inventory
    for i in range(len(slots)):
        new_item: Item 
        if 0 <= i < 3:
            new_item = Item(ItemType.PEPSI, 12)
        if 3 <= i < 5:
            new_item = Item(ItemType.COKE, 9)
        if 5 <= i < 7:
            new_item = Item(ItemType.SODA, 7)
        if 7 <= i < 10:
            new_item = Item(ItemType.WATER, 13)

        slots[i].item = new_item
        slots[i].sold_out = False

def display_inventory(vending_macine: VendingMachine) -> None:
    slots = vending_macine.inventory.inventory
    for slot in slots:
        if slot and slot.item:
            print(
                f"Code : {slot.code} "
                f"Item : {slot.item.item_type.name} "
                f"Price : {slot.item.price} "
                f"Is Available : {not slot.sold_out} "
            )

def main():

    vending_machine = VendingMachine()

    print("|")
    print("Filling Up Inventory")
    print("|")

    fill_inventory(vending_machine)
    display_inventory(vending_machine)

    print("|")
    print("Clicking on Insert Coin button")
    print("|")

    vending_state = vending_machine.vending_machine_state
    vending_state.click_on_insert_coin_button(vending_machine)

    vending_state = vending_machine.vending_machine_state
    vending_state.insert_coin(vending_machine, Coin.NICKEL)
    vending_state.insert_coin(vending_machine, Coin.QUARTER)
    
    print("|")
    print("Clicking on Product Selection button")
    print("|")

    vending_state.click_on_start_product_selection_button(vending_machine)
    vending_state = vending_machine.vending_machine_state
    vending_state.choose_product(vending_machine, 102)

    display_inventory(vending_machine)

    

if __name__ == "__main__":
    main()