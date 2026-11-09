from expense import (
    add_expense,
    view_expenses,
    calculate_total,
    search_category,
    delete_expense
)


def display_expenses(expenses):
    if not expenses:
        print("\nNo expenses found. Try adding some!")
        return

    print("\nID | Date | Category | Amount | Description")
    print("-" * 65)

    for item in expenses:
        print(
            f'{item["id"]} | {item["date"]} | '
            f'{item["category"]} | Rs.{float(item["amount"]):.2f} | '
            f'{item["description"]}'
        )


def main():
    while True:
        print("\n====== PERSONAL EXPENSE TRACKER ======")
        print("1. Add Expense.")
        print("2. View Expenses.")
        print("3. Calculate Total.")
        print("4. Search by Category.")
        print("5. Delete by Category.")
        print("6. Exit!.")

        choice = input("\nEnter your choice: ").strip()

        try:
            if choice == "1":
                category = input("Category: ")
                amount = input("Amount: ")
                description = input("Description: ")

                expense_id = add_expense(
                    category, amount, description
                )

                print(f"Expense added successfully! ID: {expense_id}")

            elif choice == "2":
                display_expenses(view_expenses())

            elif choice == "3":
                print(
                    f"\nTotal Spending of a day is: Rs.{calculate_total():.2f}"
                )

            elif choice == "4":
                category = input("Enter expense category to search: ")

                results = search_category(category)

                if results:
                    print(f"\nExpenses found in category: {category}")
                    display_expenses(results)
                else:
                    print(f"\nCategory '{category}' not found.")
            elif choice == "5":
                category = input(
                    "Enter Expense Category to delete: "
                )

                deleted_count = delete_expense(category)

                if deleted_count > 0:
                    print(
                        f"Successfully deleted {deleted_count} "
                        f"expense(s) from category '{category}'."
                    )

                else:
                    print("Expense Category not found.")

            elif choice == "6":
                print("Thank you for using Expense Tracker!")
                break

            else:
                print("Invalid choice. Enter 1 to 6.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()