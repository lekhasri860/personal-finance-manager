from collections import defaultdict

def total_expenses(expenses):
    return sum(exp.amount for exp in expenses)

def average_expense(expenses):
    if not expenses:
        return 0.0
    return total_expenses(expenses) / len(expenses)

def category_wise_summary(expenses):
    summary = defaultdict(float)
    for exp in expenses:
        summary[exp.category] += exp.amount
    return dict(summary)

def monthly_report(expenses, year_month):
    # year_month example: '2025-02'
    monthly = [exp for exp in expenses if exp.date.strftime('%Y-%m') == year_month]
    total = total_expenses(monthly)
    summary = category_wise_summary(monthly)
    return monthly, total, summary

def search_expenses(expenses, keyword):
    keyword = keyword.lower().strip()
    return [exp for exp in expenses if keyword in exp.description.lower() or keyword in exp.category.lower()]

def print_general_report(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n=== General Report ===")
    print(f"Total expenses: ₹{total_expenses(expenses):.2f}")
    print(f"Average expense: ₹{average_expense(expenses):.2f}")
    print("\nBy category:")
    for cat, amt in sorted(category_wise_summary(expenses).items()):
        print(f"  {cat}: ₹{amt:.2f}")
    print("======================")