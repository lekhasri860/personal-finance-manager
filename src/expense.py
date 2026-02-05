from datetime import date

class Expense:
    def __init__(self, amount, category, date_str, description):
        self.amount = amount
        self.category = category
        self.date = date.fromisoformat(date_str)
        self.description = description

    def __str__(self):
        return f"{self.date} | {self.category}: ₹{self.amount:.2f} - {self.description}"