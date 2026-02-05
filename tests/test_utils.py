import unittest
from src.utils import validate_amount, validate_date, validate_category, validate_description

class TestUtils(unittest.TestCase):

    def test_validate_amount_good(self):
        self.assertEqual(validate_amount("150.75"), 150.75)
        self.assertEqual(validate_amount("500"), 500.0)

    def test_validate_amount_bad(self):
        with self.assertRaises(ValueError):
            validate_amount("abc")
        with self.assertRaises(ValueError):
            validate_amount("-10")
        with self.assertRaises(ValueError):
            validate_amount("0")

    def test_validate_date_good(self):
        self.assertEqual(validate_date("2025-02-05"), "2025-02-05")
        self.assertEqual(validate_date(" 2024-12-31 "), "2024-12-31")  # should strip spaces

    def test_validate_date_bad(self):
        with self.assertRaises(ValueError):
            validate_date("2025-13-01")   # invalid month
        with self.assertRaises(ValueError):
            validate_date("bad-date")
        with self.assertRaises(ValueError):
            validate_date("2025/02/05")   # wrong format

    def test_validate_category_good(self):
        self.assertEqual(validate_category("food"), "Food")
        self.assertEqual(validate_category("OTHER"), "Other")

    def test_validate_category_bad(self):
        with self.assertRaises(ValueError):
            validate_category("InvalidCat")

    def test_validate_description_good(self):
        self.assertEqual(validate_description("Bought groceries"), "Bought groceries")

    def test_validate_description_bad(self):
        with self.assertRaises(ValueError):
            validate_description("   ")  # only spaces
        with self.assertRaises(ValueError):
            validate_description("")     # empty

if __name__ == '__main__':
    unittest.main()