from datetime import datetime

CATEGORIES = ['Food', 'Transport', 'Entertainment', 'Shopping', 'Other']

def validate_amount(input_str):
    try:
        amount = float(input_str)
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        return amount
    except ValueError:
        raise ValueError("Invalid amount. Please enter a positive number.")

def validate_category(input_str):
    input_str = input_str.strip().title()
    if input_str in CATEGORIES:
        return input_str
    raise ValueError(f"Invalid category. Choose from: {', '.join(CATEGORIES)}")

def validate_date(input_str):
    try:
        dt = datetime.strptime(input_str.strip(), '%Y-%m-%d')
        return input_str.strip()
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD (example: 2025-02-05)")

def validate_description(input_str):
    cleaned = input_str.strip()
    if not cleaned:
        raise ValueError("Description cannot be empty.")
    return cleaned

def get_input(prompt, validator):
    while True:
        try:
            value = input(prompt).strip()
            return validator(value)
        except ValueError as e:
            print(f"Error: {e}")