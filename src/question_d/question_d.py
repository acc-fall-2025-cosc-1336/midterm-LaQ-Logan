def get_bonus_pay_amount(sales): # Calculates the bonus pay amount based on sales
    sales = float(sales) # Decimal numbers taken
    if sales in range (0, 500): # (0-499)
        rate = 0.05 # 5%
    elif sales in range (500, 1000): # (500-999)
        rate = 0.06 # 6%
    elif sales in range (1000, 1500): # (1000-4999)
        rate = 0.07 # 7% 
    elif sales in range (1500, 2000): # (1500-1999)
        rate = 0.08 # 8%
    else: # (2000 and above)
        print("No bonus pay for sales of $2000 or more.") # Out of range for bonus
        rate = 0 # there are no bonuses
    bonus_pay = sales * rate # Bonus pay calculation
    return bonus_pay, rate # Returns the bonus pay and rate

def give_bonus_pay(): # Function to get user input and display bonus pay
    while True: # Loop to ensure valid input
        try:
            sales = float(input("Enter the sales amount: ")) # User input for sales amount
        except ValueError: # Error handling for invalid input
            print("Invalid input. Please enter a numeric value.")
            continue
        bonus = get_bonus_pay_amount(sales) # Calls the function to calculate bonus pay
        print(f"Bonus Pay Amount is: ${bonus[0]:.2f} at a rate of {bonus[1]*100:.0f}%") # Displays the bonus pay and rate

        again = input("Do you want to calculate another bonus pay? Enter (y/n): ") # Calculate another bonus
        if again != 'y': # Exit program
            print("Exiting the program.")
            break