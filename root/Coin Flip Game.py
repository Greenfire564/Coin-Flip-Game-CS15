import random

points = 10

print("Welcome to the Coin Flip Game: Wager Edition!")
print("You start with 10 points. Try not to run out!\n")

while points > 0:
    print(f"Current Points: {points}")

    while True:
        wager_input = input(f"Enter your wager (1 to {points}, or '0' to quit): ").strip()

        if wager_input.isdigit():
            wager = int(wager_input)
            if 0 <= wager <= points:
                break
        print(f"Invalid wager! Please enter a whole number between 0 and {points}.")

    if wager == 0:
        print(f"You walked away with {points} points. Thanks for playing!")
        break

    coin = random.choice(["heads", "tails"])

    while True:
        guess = input("Guess Heads or Tails: ").strip().lower()
        if guess in ["heads", "tails"]:
            break
        print("Invalid input! Please enter 'Heads' or 'Tails'.")

    if guess == coin:
        points += wager
        print(f"Correct! The coin was {coin.capitalize()}. You won {wager} points!\n")
    else:
        points -= wager
        print(f"Incorrect! The coin was {coin.capitalize()}. You lost {wager} points.\n")

if points == 0:
    print("Game Over! You ran out of points.")