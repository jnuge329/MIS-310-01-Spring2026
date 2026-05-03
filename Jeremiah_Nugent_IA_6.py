
# In[1]:
# Jeremiah Nugent- IA #6

def main():

    # Function to set the user's daily steps goal
    def set_steps_goal():
        
        goal = int(input("Enter your daily steps goal: "))
        return goal

    # Define a function to record daily steps for each day of the week
    def record_daily_steps():
        
        total_steps = 0
        # Day counter for the while loop
        day = 1

        # Loop once for each day of the week (7 times total) and user input
        while day <= 7:
            
            steps = int(input(f"Enter steps taken on day {day}: "))
           
            total_steps = total_steps + steps
           
            day = day + 1

        return total_steps

    # Define a function to evaluate the user's weekly performance
    def evaluate_weekly_performance(total_steps, goal):
        # Calculate the average steps per day for the week
        average_steps = total_steps / 7

        # Display the user's average daily steps
        print(f"Your average daily steps for the week: {average_steps:.2f}")

        # Compare average steps with the daily goal and display result
        if average_steps > goal:
            print(f"You exceeded your daily steps goal of {goal} steps on average, fantastic job!")
        elif average_steps == goal:
            print(f"You met your daily steps goal of {goal} steps on average this week, congrats!")
        else:
            print(f"You did not meet your daily steps goal of {goal} steps on average. Try again next week!")

    # Call set_steps_goal to get the user's daily steps goal
    goal = set_steps_goal()

    # Call record_daily_steps to collect and total the steps for the week
    total_steps = record_daily_steps()

    # Call evaluate_weekly_performance to assess and display the results
    evaluate_weekly_performance(total_steps, goal)

main()

