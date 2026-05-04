import random


user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print(" Welcome to Rock-Paper-Scissors Game!")

while True:

    user = input("\nEnter rock, paper, or scissors: ").lower()


    if user not in choices:
        print(" Invalid input! Please try again.")
        continue


    computer = random.choice(choices)


    print("You chose:", user)
    print("Computer chose:", computer)


    if user == computer:
        print(" It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("🎉 You win!")
        user_score += 1
    else:
        print("💻 Computer wins!")
        computer_score += 1


    print(f"Score → You: {user_score} | Computer: {computer_score}")


    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        break


print("\n Final Score")
print(f"You: {user_score} | Computer: {computer_score}")

if user_score > computer_score:
    print("🏆 Congratulations! You are the overall winner!")
elif user_score < computer_score:
    print("💻 Computer is the overall winner!")
else:
    print("🤝 It's an overall tie!")

print("Thanks for playing! 🎮")