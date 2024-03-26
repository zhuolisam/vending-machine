from typing import Dict

NotesTray = Dict[int, int]
ItemsPrice = Dict[str, int]


class VendingMachine:
    def __init__(self, notes_tray: NotesTray, items_price: ItemsPrice) -> None:
        if notes_tray:
            self.notes_tray = notes_tray
        else:
            self.notes_tray = {
                50: 4,  # notes: quantity
                10: 4,
                5: 10,
                1: 20,
            }

        if items_price:
            self.items_price = items_price
        else:
            self.items_price = {
                "Coke": 10,
                "Pepsi": 10,
                "Tea": 10,
            }

    def get_menu(self):
        return self.items_price

    def get_change(self, change: int):
        if change == 0:
            return {}

        transaction = self.notes_tray.copy()
        return_notes = {}

        for note in transaction:
            note_quantity = change // note  # number of current notes required

            if note_quantity == 0:
                continue

            # if ample notes are available
            if note_quantity <= transaction[note]:
                change = change % note
                transaction[note] -= note_quantity
                return_notes[note] = note_quantity
            # if not ample notes available
            else:
                change -= note * transaction[note]
                transaction[note] = 0
                return_notes[note] = transaction[note]

            if change == 0:
                break

        if change > 0:
            raise Exception("Insufficient change")
        else:
            # transaction successful, update notes_tray
            for note in return_notes:
                self.notes_tray[note] -= return_notes[note]

        return return_notes

    def get_item_price(self, item_name: str):
        if item_name not in self.items_price:
            raise Exception("No such item")
        return self.items_price[item_name]

    def buy_item(self, item_name: str, amount_paid: int):
        # get item price
        item_price = self.get_item_price(item_name)

        # check amount paid
        if amount_paid < item_price:
            raise Exception("Insufficient amount paid")

        # return balance
        balance = amount_paid - item_price
        return_notes = self.get_change(balance)

        return item_name, balance, return_notes


def main():
    # set up
    vending_machine = VendingMachine(notes_tray=None, items_price=None)
    # display menu
    menu = vending_machine.get_menu()
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: RM{price} ")

    # example purchase
    item_name = "Coke"
    amount_paid = 15

    item, balance, change = vending_machine.buy_item(item_name, amount_paid)
    print(balance, change)


if __name__ == "__main__":
    main()
