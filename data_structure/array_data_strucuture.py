# List of monthly expenses
list_of_monthly_expenses = [2200, 2350, 2600, 2130, 2190]

# 1. How much more did you spend in February compared to January?
extra_spent_in_feb = list_of_monthly_expenses[1] - list_of_monthly_expenses[0]
print("You spent", extra_spent_in_feb, "dollars more in February compared to January.")

# 2. Total expense in the first quarter (first three months)
total_first_quarter = sum(list_of_monthly_expenses[:3])
print("Total expense in the first quarter is:", total_first_quarter)

# 3. Check if any month had exactly 2000 dollars in expenses
spent_2000 = 2000 in list_of_monthly_expenses
print("Did you spend exactly 2000 dollars in any month?", spent_2000)

# 4. Adding June's expense to the list
list_of_monthly_expenses.append(1980)
print("Updated monthly expenses after adding June:", list_of_monthly_expenses)

# 5. Correcting April's expense after getting a 200 dollar refund
list_of_monthly_expenses[3] -= 200
print("Updated expenses after the refund in April:", list_of_monthly_expenses)
