def display_menu(): #will display the menu options
    print("Menu (Select an Option):")
    print("1. Play Game") 
    print("2. Exit")
    
    
def run_menu(): #will run the menu and get user input
    display_menu()
    choice = input("Enter your choice (1-2): ")
    handle_choice(choice)

def handle_choice(choice): #will handle the user's choice
    if choice == '1':
        print("Starting the game...")
        play_game() #will start the game
    elif choice == '2':
        print("Exiting the game. Goodbye!") #will exit the game
    else:
        print("Invalid choice. Please try again.") #user input invalid

import random #will import the random module

def get_random_number(): #will get a random number between 1 and 5
    return random.randint(1, 5) 
   
   
def play_game(): #will run the game
   while True:
        num = get_random_number()
        guessed = False #the user has not guessed the number yet
        
        while not guessed:
            try:
                guess = int(input("Guess a number between 1 and 5: ")) #will get user input
                if guess < 1 or guess > 5: #will check if the input is in range
                    print("Please enter a number between 1 and 5.")
                elif guess == num: #user input matches the random number
                    print("Congratulations! You guessed the correct number.")
                    guessed = True
                else:
                    print("Incorrect guess. Try again.") #user input does not match the random number
            except ValueError:
                print("Invalid input. Please enter a number.") #invalid user input
        
        while True:
            play_again = input("Do you want to play again? (y/n): ").lower() #will ask to start a new game
            if play_again == 'y':
                break
            elif play_again == 'n': #will exit the game
                print("Thanks for playing! Goodbye!")
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.") #invalid user input


    