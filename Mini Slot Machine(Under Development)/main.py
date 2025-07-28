import random

def slot_machine():
    # This will define the values of a each symbols
    symbols = {
        '🌶': 2, 
        '🍑': 5,
        '🎱': 15,
        '💰': 50,      
        '👊': 25,         
    }

    

# This will ask the user to input their amount of deposit
def get_deposit():
    while True:
        amount = int(input("Enter the amount you want to deposit: $"))
        if amount > 0:
            print(f"You have now a balance of {amount}")
            break
        else:
            print("Invalid user input!")
    return amount

# This will ask the user to input their amount of bet
def get_bet(deposit):
    while True:
        amount = int(input("How much would you like to bet: "))
        if amount > deposit:
            print("You have insufficient amount of deposit")
        else:
            break
    return amount

# This will be the main function of running the entire code
def main():
    deposit = get_deposit()
    bet = get_bet(deposit)
    print(f"You now have bet ${bet} and now you have a new balance of ${deposit - bet}")

main()