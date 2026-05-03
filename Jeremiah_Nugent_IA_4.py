
# In[1]:
#Problem #1- Max Sales by Weekday

#Introduction
print("Finding maximum weekday sales by days.")

#Week days and sales
Weekday_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
Sales_per_day_list = [50, 75, 150, 125, 100]

# Finding highest sales day with f-strings
#Monday start
max_sales = Sales_per_day_list[0]
max_index = 0

if Sales_per_day_list[1] > max_sales:
    max_sales = Sales_per_day_list[1]
    max_index = 1

if Sales_per_day_list[2] > max_sales:
    max_sales = Sales_per_day_list[2]
    max_index = 2

if Sales_per_day_list[3] > max_sales:
    max_sales = Sales_per_day_list[3]
    max_index = 3

if Sales_per_day_list[4] > max_sales:
    max_sales = Sales_per_day_list[4]
    max_index = 4

#Finalizing calculation for highest sales
max_day = Weekday_list[max_index]

#Display highest result and week day
print(f"The Max sales is ${max_sales}")
print(f"The Max sales day is {max_day}")

# In[2]:
#Problem #2- Range for series

#Create empty list for input numbers
numbers = []

#Incorporate users' input numbers until 0 is given to end
value = float(input("Enter value: "))

while value != 0:
    if value > 0:                
        numbers.append(value)
    else:
        print("No negative numbers are not allowed, re-enter a positive number or 0 to finish.")
    
    value = float(input("Enter value (or 0 to end): "))
#Display values in the list
print(numbers)

#Calculate range if/when positive values are inputted
if numbers:
    min_val = numbers[0]
    max_val = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] < min_val:
            min_val = numbers[i]
        if numbers[i] > max_val:
            max_val = numbers[i]
        i += 1

#Display Range results post calculations 
    print(f"Range= {max_val - min_val}")

# In[3]:
