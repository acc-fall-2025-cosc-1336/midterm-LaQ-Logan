def get_day_of_week(day):
    if day == 1:
        return "Monday"
    elif day == 2:  
        return "Tuesday"
    elif day == 3:
        return "Wednesday"
    elif day == 4:
        return "Thursday"
    elif day == 5:
        return "Friday"
    elif day == 6:
        return "Saturday"
    elif day == 7:
        return "Sunday"
    else:
        return "Invalid, please enter a number between 1 and 7."
    
def convert_day_number():
    while True:
        try:
            num = int(input("Enter a number between (1-7) to receive a day: "))
            day = get_day_of_week(num)
            print(day)
        except ValueError:
            print("Invalid input, please enter a number between (1-7).")
            continue
        
        again = input("Do you want to convert another number? (y/n): ")
        if again != 'y':
                print("Exiting, goodbye!")
                break