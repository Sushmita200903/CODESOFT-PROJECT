import random

# Define the list of choices
choices = ["rock", "paper", "scissor"]

# Initialize scores
user_score = 0
computer_score = 0

# Game loop
while True:
    # Get the user's choice
    user_choice = input("Enter your choice (rock, paper, or scissor): ").lower()

    # Check if the user's choice is valid
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, or scissor): ").lower()

    # Get the computer's choice
    computer_choice = random.choice(choices)

    # Display the choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the result
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        print("You win this round!")
        user_score += 1
    else:
        print("You lose this round!")
        computer_score += 1

    # Display current scores
    print(f"Scores -> You: {user_score}, Computer: {computer_score}")

    # Ask if the user wants to play another round
    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        break

# Final scores
print("\nGame Over!")
print(f"Final Scores -> You: {user_score}, Computer: {computer_score}")

# Determine the overall winner
if user_score > computer_score:
    print("Congratulations! You are the overall winner!")
elif user_score < computer_score:
    print("Better luck next time! The computer is the overall winner.")
else:
    print("It's an overall tie!")
