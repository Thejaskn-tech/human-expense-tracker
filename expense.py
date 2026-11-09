import csv
from pathlib import Path
from datetime import date
import math

FILE = Path(__file__).parent / "expenses.csv"

FIELDS = ["id", "date", "category", "amount", "description"]


# Load expenses from CSV
def load_expenses():
    if not FILE.exists():
        return []

    with open(FILE, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# Save expenses into CSV
def save_expenses(expenses):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)


# Add a new expense
def add_expense(category, amount, description):
    category = category.strip()
    description = description.strip()

    if not category or not description:
        raise ValueError("Category and description cannot be empty.")

    try:
        amount = round(float(amount), 2)
    except (ValueError, TypeError):
        raise ValueError("Enter a valid amount.") from None

    if not math.isfinite(amount) or amount <= 0:
        raise ValueError("Amount must be positive and finite.")

    expenses = load_expenses()

    new_id = max(
        (int(item["id"]) for item in expenses),
        default=0
    ) + 1

    expenses.append({
        "id": str(new_id),
        "date": date.today().isoformat(),
        "category": category,
        "amount": f"{amount:.2f}",
        "description": description
    })

    save_expenses(expenses)

    return new_id


# View all expenses
def view_expenses():
    return load_expenses()


# Calculate total expenses
def calculate_total(expenses=None):
    if expenses is None:
        expenses = load_expenses()

    return round(
        sum(float(item["amount"]) for item in expenses), 2
    )


# Search expenses by category
def search_category(category):
    category = category.strip().lower()

    return [
        item for item in load_expenses()
        if item["category"].strip().lower() == category
    ]


# Delete expenses by category
def delete_expense(category):
    category = category.strip().lower()

    if not category:
        return 0

    expenses = load_expenses()

    updated_expenses = [
        item for item in expenses
        if item["category"].strip().lower() != category
    ]

    deleted_count = len(expenses) - len(updated_expenses)

    if deleted_count > 0:
        save_expenses(updated_expenses)

    return deleted_count