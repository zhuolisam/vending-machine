import unittest
from vending_machine import VendingMachine


class TestVendingMachine(unittest.TestCase):
    def test_buy_item_with_insufficient_amount_paid(self):
        notes_tray = {50: 4, 10: 4, 5: 10, 1: 20}
        items_price = {"Coke": 10, "Pepsi": 15, "Tea": 20}
        vm = VendingMachine(notes_tray, items_price)

        with self.assertRaises(Exception) as context:
            vm.buy_item("Coke", 5)
        self.assertEqual(str(context.exception), "Insufficient amount paid")

    def test_buy_item_with_insufficient_change(self):
        notes_tray = {50: 0, 10: 0, 5: 0, 1: 0}
        items_price = {"Coke": 10, "Pepsi": 15, "Tea": 20}
        vm = VendingMachine(notes_tray, items_price)

        with self.assertRaises(Exception) as context:
            vm.buy_item("Pepsi", 20)
        self.assertEqual(str(context.exception), "Insufficient change")

    def test_buy_item_with_valid_purchase(self):
        # Initialize a VendingMachine instance
        notes_tray = {50: 4, 10: 4, 5: 10, 1: 20}
        items_price = {"Coke": 10, "Pepsi": 15, "Soda": 20}
        vm = VendingMachine(notes_tray, items_price)

        # Test buy_item() with a valid purchase
        item, balance, change = vm.buy_item("Coke", 20)
        self.assertEqual(item, "Coke")
        self.assertEqual(balance, 10)
        self.assertEqual(change, {10: 1})

    def test_buy_item_with_exact_amount_paid(self):
        # Initialize a VendingMachine instance
        notes_tray = {50: 4, 10: 4, 5: 10, 1: 20}
        items_price = {"Coke": 10, "Pepsi": 15, "Soda": 20}
        vm = VendingMachine(notes_tray, items_price)

        # Test buy_item() with exact amount paid
        item, balance, change = vm.buy_item("Coke", 10)
        self.assertEqual(item, "Coke")
        self.assertEqual(balance, 0)
        self.assertEqual(change, {})


if __name__ == "__main__":
    unittest.main()
