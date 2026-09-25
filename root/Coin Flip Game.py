import random

points = 10

print("Coin Flip Game")
print("You start with 10 points.\n")

while points > 0:
    print(f"Current Points: {points}")

    while True:
        wager_input = input(f"Enter your wager (1 to {points}, or '0' to quit): ")
        if wager_input.isdigit():
            wager = int(wager_input)
            if 0 <= wager <= points:
                break
        print(f"Only allowed number between 1 and {points} points.")

    if wager == 0:
        print(f"You got {points} points.")
        break

    coin = random.choice(["heads", "tails"])

    while True:
        guess = input("Guess Heads or Tails: ")
        if guess in ["heads", "tails"]:
            break
        print("Invalid input! Please enter 'Heads' or 'Tails'.")

    if guess == coin:
        points += wager
        print(f"Correct! The coin was {coin}. You won {wager} points!\n")
    else:
        points -= wager
        print(f"Incorrect! The coin was {coin} You lost {wager} points.\n")

if points == 0:
    print("Game Over You ran out of points.")

