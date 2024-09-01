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

# List of heroes
heros = ["spider man", "thor", "hulk", "iron man", "captain america"]

# 1. Print the number of heroes in the list
print("Length of the list:", len(heros))

# 2. Add 'black panther' to the end of the list
heros.append("black panther")

# 3. You realize that 'black panther' should be placed after 'hulk'.
#    First, remove 'black panther' from the end and then insert it after 'hulk'.
heros.remove("black panther")  # Remove 'black panther'
index_of_hulk = heros.index("hulk")  # Find the position of 'hulk'
heros.insert(index_of_hulk + 1, "black panther")  # Insert 'black panther' after 'hulk'
print(heros)

# 4. Replace 'thor' and 'hulk' with 'doctor strange' because they get angry easily.
heros[1:3] = [
    "doctor strange"
]  # Replace items at positions 1 and 2 with 'doctor strange'
print(heros)

# 5. Sort the heroes list in alphabetical order
heros.sort()
print(heros)
