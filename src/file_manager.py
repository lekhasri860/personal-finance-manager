import csv
import os
import shutil
from .expense import Expense

DATA_DIR = 'data'
EXPENSES_FILE = os.path.join(DATA_DIR, 'expenses.csv')
BACKUP_FILE = os.path.join(DATA_DIR, 'expenses_backup.csv')

def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def save_expenses(expenses, filename=EXPENSES_FILE):
    ensure_data_dir()
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
        for expense in expenses:
            writer.writerow([expense.date.isoformat(), expense.category, expense.amount, expense.description])

def load_expenses(filename=EXPENSES_FILE):
    expenses = []
    ensure_data_dir()
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if row and len(row) == 4:
                    date_str, category, amount_str, description = row
                    try:
                        amount = float(amount_str)
                        expenses.append(Expense(amount, category, date_str, description))
                    except ValueError:
                        print(f"Warning: Skipping invalid row: {row}")
    return expenses

def backup_data():
    ensure_data_dir()
    if os.path.exists(EXPENSES_FILE):
        shutil.copy(EXPENSES_FILE, BACKUP_FILE)
        print("Data backed up successfully!")
    else:
        print("No data to backup.")

def restore_data():
    ensure_data_dir()
    if os.path.exists(BACKUP_FILE):
        shutil.copy(BACKUP_FILE, EXPENSES_FILE)
        print("Data restored successfully!")
    else:
        print("No backup file found.")