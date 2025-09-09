import random

def play_game():
    print("=" * 44)
    print("ROCK - PAPER - SCISSORS".center(44))
    print("=" * 44)

    choices = ["rock", "paper", "scissors"]

    user = input("Enter rock, paper or scissors\n(YOU) : ").lower()
    bot = random.choice(choices)
    print(f"BOT : {bot}")

    if user not in choices:
        print("Invalid choice!!")
        return

    if user == bot:
        print("It's a Tie....")
    elif (user == "rock" and bot == "scissors") or \
         (user == "paper" and bot == "rock") or \
         (user == "scissors" and bot == "paper"):
        print("CONGRATULATIONS!! You won the game....")
    else:
        print("Oops!! You lost the game....")

while True:
    play_game()
    again = input("| Would you like to play again (yes/no) | ").lower()
    if again != "yes":
        print("Thank You for playing the game")

        break
