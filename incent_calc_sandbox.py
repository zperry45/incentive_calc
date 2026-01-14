# Incentive Rate as of Jan 2026
# basic = 8.17

# hours_basic = float(input("Add your basic hours worked "))

# basic_total = (hours_basic * basic)

# total = (basic_total)

# print(f"Total Basic Incentive: ${basic_total}")

# print(f"Your Total Incentive Pay is: ${total}")

basic_tasks = []
basic_entries = int(input("Enter Basic hours worked: "))

for i in range(basic_entries):
    item = input(f"Task 1 {i+1}: ")
    basic_tasks.append(item)

print(f"The total Basic hours worked was: {basic_tasks}")

