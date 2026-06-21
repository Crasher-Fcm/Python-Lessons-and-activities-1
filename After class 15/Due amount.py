def calculate_due_amount(total_bill, amount_paid):
    """Calculates the remaining due amount after a payment."""
    # Deduct the paid amount from the total bill
    remaining_due = total_bill - amount_paid
    return remaining_due

# --- Example Usage ---
# 1. Take input from the user
try:
    bill = float(input("Enter the total bill amount: "))
    paid = float(input("Enter the amount paid by the customer: "))

    # 2. Call the function to calculate the balance
    due = calculate_due_amount(bill, paid)

    # 3. Display the result
    if due > 0:
        print(f"The customer still owes: ${due:.2f}")
    elif due == 0:
        print("The bill is fully paid. Remaining balance: $0.00")
    else:
        print(f"The customer overpaid. Change due: ${abs(due):.2f}")

except ValueError:
    print("Please enter valid numerical values for the amounts.")