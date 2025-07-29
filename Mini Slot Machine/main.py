import random as rd

def slot_machine(bet):
    # A dictionary
    symbols = {
        '🌶': 2,
        '🍑': 3,
        '🎱': 5,
        '💰': 10,
        '👊': 20
    }
    payouts = {
        3: 5,
        2: 2
    }
    # This will randomize the symbols
    reels = [rd.choice(list(symbols.keys())) for _ in range(3)]
    print(f" { '|' .join(reels)}")
    # Checks for winning combination
    if reels[0] == reels[1] == reels[2]:
        matches = 3
        matched_symbols = reels[0]
    elif reels[0] == reels[1] or reels[1] == reels[2]:
        matches = 2
        matched_symbols = reels[1]
    elif reels[0] == reels[2]:
        matches = 2
        matched_symbols = reels[0]
    else:
        matches = 0

    # Calculate winnings
    if matches >= 2:
        win_amount = symbols[matched_symbols] * payouts[matches] * bet
        print(f"Matched {matches}{matched_symbols}'s! You win ${win_amount}")
        return win_amount
    else:
        print("No winning combination, try again...")
        return 0


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
    while deposit > 0:
        bet = get_bet(deposit)
        deposit -= bet
        winnings = slot_machine(bet)
        deposit += winnings

        if deposit == 0:
            print("You've run out of money!")
            break

        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print(f"You're cashing out with ${deposit}")
            break
if __name__ == "__main__":
    main()
