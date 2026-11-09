
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch

import expense


class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.test_file = Path(self.temp.name) / "expenses.csv"
        self.patcher = patch.object(expense, "FILE", self.test_file)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        self.temp.cleanup()

    def test_add_expense(self):
        expense.add_expense("Food", 150, "Lunch")
        self.assertEqual(len(expense.load_expenses()), 1)

    def test_calculate_total(self):
        expense.add_expense("Food", 150, "Lunch")
        expense.add_expense("Travel", 50, "Bus")
        self.assertEqual(expense.calculate_total(), 200)

    def test_search_category(self):
        expense.add_expense("Food", 150, "Lunch")
        self.assertEqual(len(expense.search_category("food")), 1)

    def test_delete_expense(self):
        expense.add_expense("Food", 150, "Lunch")
        self.assertTrue(expense.delete_expense(1))
        self.assertEqual(len(expense.load_expenses()), 0)

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            expense.add_expense("Food", "abc", "Lunch")

    def test_empty_category(self):
        with self.assertRaises(ValueError):
            expense.add_expense("", 150, "Lunch")


if __name__ == "__main__":
    unittest.main()
