from .utils import get_input, validate_amount, validate_category, validate_date, validate_description, CATEGORIES
from .reports import print_general_report, monthly_report, search_expenses, category_wise_summary

def display_menu():
    print("\n" + "="*42)
    print("      PERSONAL FINANCE MANAGER")
    print("="*42)
    print("\nMAIN MENU:")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Category Summary")
    print("4. Monthly Report")
    print("5. Search Expenses")
    print("6. Backup Data")
    print("7. Restore Backup")
    print("8. Exit")
    while True:
        try:
            choice = int(input("\nEnter choice (1-8): ").strip())
            if 1 <= choice <= 8:
                return choice
            print("Please enter a number between 1 and 8.")
        except ValueError:
            print("Please enter a valid number.")

def add_expense(expenses):
    print("\n--- Add New Expense ---")
    amount = get_input("Amount (₹): ", validate_amount)
    category = get_input(f"Category ({'/'.join(CATEGORIES)}): ", validate_category)
    date_str = get_input("Date (YYYY-MM-DD): ", validate_date)
    description = get_input("Description: ", validate_description)
    
    from .expense import Expense
    expenses.append(Expense(amount, category, date_str, description))
    print("\nExpense added successfully! ✓")

def view_all_expenses(expenses):
    if not expenses:
        print("\nNo expenses yet.")
        return
    print("\n--- All Expenses (sorted by date) ---")
    for exp in sorted(expenses, key=lambda e: e.date):
        print(exp)

def view_category_summary(expenses):
    summary = category_wise_summary(expenses)
    if not summary:
        print("\nNo expenses to show.")
        return
    print("\n--- Category Summary ---")
    for cat, amt in sorted(summary.items()):
        print(f"{cat:12} ₹{amt:,.2f}")
    print("------------------------")

def show_monthly_report(expenses):
    year_month = input("\nEnter month (YYYY-MM): ").strip()
    if len(year_month) != 7 or year_month[4] != '-':
        print("Invalid format. Use YYYY-MM like 2025-02")
        return
    monthly, total, summary = monthly_report(expenses, year_month)
    if not monthly:
        print(f"No expenses in {year_month}")
        return
    print(f"\n--- Report for {year_month} ---")
    print(f"Total: ₹{total:,.2f}")
    print("Categories:")
    for cat, amt in sorted(summary.items()):
        print(f"  {cat:12} ₹{amt:,.2f}")
    print("\nIndividual expenses:")
    for exp in sorted(monthly, key=lambda e: e.date):
        print(exp)

def search_menu(expenses):
    keyword = input("\nSearch keyword (in description or category): ").strip()
    if not keyword:
        print("No keyword entered.")
        return
    results = search_expenses(expenses, keyword)
    if not results:
        print("No matching expenses found.")
        return
    print(f"\nFound {len(results)} matching expense(s):")
    for exp in results:
        print(exp)