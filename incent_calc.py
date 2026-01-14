#Incentive Rate as of Jan 2026
basic = 8.17
lvl_1 = 12.27
lvl_2 = 16.17
lvl_3 = 21.53
lvl_4 = 28.15
lvl_5 = 38.96

hours_basic = float(input("Add your basic hours worked "))
hours_1 = float(input("Add your level_1 hours worked "))
hours_2 = float(input("Add your level_2 hours worked "))
hours_3 = float(input("Add your level_3 hours worked "))
hours_4 = float(input("Add your level_4 hours worked "))
hours_5 = float(input("Add your level_5 hours worked "))



basic_total = (hours_basic * basic)
h1_total= (hours_1 * lvl_1)
h2_total = (hours_2 * lvl_2)
h3_total = (hours_3 * lvl_3)
h4_total = (hours_4 * lvl_4)
h5_total = (hours_5 * lvl_5)

# total = (basic_total)
total = (basic_total + h1_total + h2_total + h3_total + h4_total + h5_total)


print(f"Total Basic Incentive: ${basic_total}")
print(f"Total Level_1 Incentive: ${h1_total}")
print(f"Total Level_2 Incentive: ${h2_total}")
print(f"Total Level_3 Incentive: ${h3_total}")
print(f"Total Level_4 Incentive: ${h4_total}")
print(f"Total Level_5 Incentive: ${h5_total}")

print(f"Your Total Incentive Pay is: ${total}")

