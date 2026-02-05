import sys
import os

print("=== DEBUG ===")
print("Current working directory:", os.getcwd())
print("Looking for data folder at:", os.path.abspath("data"))
print("=== DEBUG END ===")

from src.file_manager import load_expenses, save_expenses, backup_data, restore_data
from src.menu import (
    display_menu,
    add_expense,
    view_all_expenses,
    view_category_summary,
    show_monthly_report,
    search_menu
)

def main():
    print("Loading expenses...")
    expenses = load_expenses()
    print(f"Loaded {len(expenses)} expenses.")

    print("Welcome to Personal Finance Manager!")

    while True:
        try:
            choice = display_menu()

            if choice == 1:
                add_expense(expenses)
                print("Saving after add...")
                save_expenses(expenses)
                print("→ Successfully saved after adding expense")

            elif choice == 2:
                view_all_expenses(expenses)

            elif choice == 3:
                view_category_summary(expenses)

            elif choice == 4:
                show_monthly_report(expenses)

            elif choice == 5:
                search_menu(expenses)

            elif choice == 6:
                backup_data()

            elif choice == 7:
                restore_data()
                expenses = load_expenses()
                print(f"→ Reloaded {len(expenses)} expenses after restore")

            elif choice == 8:
                print("Saving before exit...")
                save_expenses(expenses)
                print("Data saved successfully. Goodbye!")
                sys.exit(0)

            input("\nPress Enter to continue...")

        except KeyboardInterrupt:
            print("\nCaught Ctrl+C → Saving before exit...")
            save_expenses(expenses)
            print("Data saved safely.")
            sys.exit(1)

        except Exception as e:
            print(f"Error: {e}")
            print("Trying to save anyway...")
            save_expenses(expenses)
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()