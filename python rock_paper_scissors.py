# Rock-Paper-Scissors Game
# TASK 4

import random

# Score variables
user_score = 0
computer_score = 0

print("===================================")
print("   ROCK PAPER SCISSORS GAME")
print("===================================")
print("Instructions:")
print("Choose Rock, Paper, or Scissors")
print("Type 'exit' anytime to quit the game")
print("===================================\n")

# Game loop
while True:

    # User input
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    # Exit condition
    if user_choice == "exit":
        print("\nThanks for playing!")
        break

    # Validate input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.\n")
        continue

    # Computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Display choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    # Display scores
    print("\nCurrent Score:")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score:")
        print(f"You: {user_score}")
        print(f"Computer: {computer_score}")
        print("\nThanks for playing!")
        break

    print("\n-----------------------------------\n")
