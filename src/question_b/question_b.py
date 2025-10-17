def is_prime(num): # checks if num is prime
    if num <= 1:
        return False # 0 and 1 are not prime numbers
    for i in range(2, int(num**0.5) + 1): # num**0.5 = num^1/2 sq rt, int(num**0.5) +1 checks for divisors greater than sq rt
        if num % i == 0: # if num is divisible by i, it is not prime
            return False # num is not prime
    return True # num is prime

def check_if_prime(): # handles user input and output and loops until user decides to exit
    while True:
        try: #starts loop until user decides to exit
            num = int(input("Enter a number to check if it's prime: ")) # gets user input 
        except ValueError: # handles invalid input
            print("Invalid input. Please enter a valid integer.")
            continue # restarts the loop if input is invalid
    
        if is_prime(num): # calls is_prime function to check if num is prime
            print(f"{num} is a prime number.")
        else:   # handles non prime numbers
            print(f"{num} is not a prime number.")
    
        again = input("Do you want to check another number? (yes/no): ") #Either continues or exits the loop
        if again != 'yes':
            print("Exiting the program.")
            break # exits the loop





