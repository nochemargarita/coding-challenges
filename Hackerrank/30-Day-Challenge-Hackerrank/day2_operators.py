# Objective 
# In this challenge, you'll work with arithmetic operators.

# Task 
# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

# Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

# Input Format

# There are 3 lines of numeric input: 
# The first line has a double, mealCost(the cost of the meal before tax and tip). 
# The second line has an integer, tipPercent(the percentage of  mealCost being added as tip). 
# The third line has an integer, taxPercent(the percentage of  mealCost being added as tax).

# Output Format

# Print the total meal cost, where totalCost is the rounded integer result of the entire bill (mealCost with added tax and tip).

# # Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

    tip = meal_cost * (tip_percent/float(100))
    tax = meal_cost * (tax_percent/float(100))
    

    total = meal_cost + tip + tax
    print int(round(total))

# Input1:
# meal_cost = 12.00
# tip_percent = 20
# tax_percent = 8

# # Output1:
# total = 15


# Input2:
# meal_cost = 10.25
# tip_percent = 17
# tax_percent = 5

# Output2:
# total = 13

