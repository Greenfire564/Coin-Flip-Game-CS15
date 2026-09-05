import random

while True:
    coin = random.choice(["heads", "tails"])

    while True:
        guess = input("Guess Heads or Tails (or 'quit' to exit): ").strip().lower()

        if guess in ["heads", "tails", "quit"]:
            break
        else:
            print("Invalid input. Please enter 'Heads' or 'Tails'.")

    if guess == "quit":
        print("Thanks for playing!")
        break

    if guess == coin:
        print(f"Correct! The coin landed on {coin.capitalize()}.\n")
    else:
        print(f"Incorrect! The coin landed on {coin.capitalize()}.\n")