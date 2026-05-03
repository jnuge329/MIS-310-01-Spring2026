#This file is my third Individual assignment in the course.
# In[1]:
# Problem #1 Part A
#Basic repetition 

target = float(input("Enter total sales target for 5 days (in $): "))

cumulative = 0.0

for day in range(1, 6):
    sales = float(input(f"Enter day {day} total sales: "))
    cumulative += sales
    percentage = (cumulative / target) * 100
    print(f"Total sales across 5-day timeframe: {cumulative:.1f} ({percentage:.1f} %)")

# In[2]:
# Part (B) with input validation

while True:
    try:
        target = float(input("Enter total sales target: "))
        if target <= 0:
            print("Error: Sales target must be greater than zero.")
            continue
        break
    except ValueError:
        print("Error: Please enter a valid number greater than zero.")

cumulative = 0.0

for day in range(1, 6):
    while True:
        try:
            sales = float(input(f"Enter day {day} sales: "))
            if sales <= 0:
                print("Error: Sales cannot be zero or negative.")
                continue
            break 
        except ValueError:
            print("Error: Please enter a valid positive number.")
    
    cumulative += sales
    percentage = (cumulative / target) * 100
    print(f"Cumulative sales after last input (target percentage): {cumulative:.1f} ({percentage:.1f} %)")


# In[3]:
#Problem 2, Part A- Shuttle Route Timing and Distance Loop
print("Shuttle Route Time Calculator\n")
print(" *All speeds and distance numbers must be positive*")

route_number = 1
fastest_time = float('inf')     
fastest_route = None

#Receive input for distance and speed
while True:

    distance = float(input(f"Enter route {route_number} distance (miles): "))
    speed = float(input(f"Enter route {route_number} speed (miles/hour): "))
    
#Calculating time in minutes and hours
    time_hours = distance / speed
    time_minutes = time_hours * 60
    
#Display results from calculation
    print(f"Route {route_number} time: {time_minutes:.0f} minutes\n")

#Route Comparison
    if time_minutes < fastest_time:
        fastest_time = time_minutes
        fastest_route = route_number
    
# Ask if more routes
    more = input("More routes (y/n)?: ").strip().lower()
    if more != 'y':
        break
    
    route_number += 1

# Display final route and time results
if fastest_route is not None:
    print(f"Route {fastest_route} is fastest, Total route time: {fastest_time:.0f} minutes")
else:
    print("No routes were entered.")

# ##### Problem 2, Part B- Data table implementation
# 
# print("Shuttle Route Time Calculator\n")
# print("* All speeds and distances must be positive *\n")
# 
# route_number = 1
# fastest_time = float('inf')     
# fastest_route = None
# 
# while True:
#     # Get inputs
#     distance = float(input(f"Enter route {route_number} distance (miles): "))
#     speed = float(input(f"Enter route {route_number} speed (miles/hour): "))
#     
#     # Calculate time
#     time_hours = distance / speed
#     time_minutes = time_hours * 60
#     
#     # Show result for this route
#     print(f"Route {route_number} time: {time_minutes:.0f} minutes\n")
#     
#     # Update fastest route if this one is quicker
#     if time_minutes < fastest_time:
#         fastest_time = time_minutes
#         fastest_route = route_number
#     
#     # Ask to continue
#     more = input("More routes (y/n)?: ").strip().lower()
#     if more != 'y':
#         break
#     
#     route_number += 1
# 
# # Final result
# if fastest_route is not None:
#     print(f"Route {fastest_route} is fastest; {fastest_time:.0f} minutes")
# else:
#     print("No routes were entered.")

# In[4]:
# Problem 2, Part C - Shuttle Route Timing and Distance Enhanced

print("Shuttle Route Time Calculator (with validation)\n")

route_number = 1
fastest_time = float('inf')
fastest_route = None

while True:
#Receive valid distance inputs
    while True:
        try:
            distance = float(input(f"Enter route {route_number} distance (miles): "))
            if distance <= 0:
                print("Error: Distance must be greater than 0.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number.")
    
# Receive valid speed inputs
    while True:
        try:
            speed = float(input(f"Enter route {route_number} speed (miles/hour): "))
            if speed <= 0:
                print("Error: Speed must be greater than 0.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number.")
    
#Time Calculations for minutes and hours
    time_hours = distance / speed
    time_minutes = time_hours * 60
    
    print(f"Route {route_number} time: {time_minutes:.0f} minutes\n")
    
#Tracking the fastest route
    if time_minutes < fastest_time:
        fastest_time = time_minutes
        fastest_route = route_number
    
# Ask for more routes
    while True:
        more = input("More routes (y/n)?: ").strip().lower()
        if more in ['y', 'n']:
            break
        print("Please enter 'y' or 'n'.")
    
    if more == 'n':
        break
    
    route_number += 1

# Final result
if fastest_route is not None:
    print(f"Route {fastest_route} is fastest; {fastest_time:.0f} minutes")
else:
    print("No valid routes were entered.")
