# Ask for total bill amount
total_bill = float(input("Enter total bill amount: "))

# Ask how much the customer paid
amount_paid = float(input("Enter amount paid by customer: "))

# Calculate due amount
due = total_bill - amount_paid

# Check and show result
if due > 0:
    print("Customer still has to pay Rs.", due)
elif due == 0:
    print("Bill fully paid. No due remaining.")
else:
    print("Customer overpaid by Rs.", abs(due))
