#playing rock ,paper and scissor game
import random

print("Welcome to Rock-Paper-Scissors!")
print("Enter 0 for Rock, 1 for Paper, 2 for Scissors")

user = int(input("Your choice: "))
computer = random.randint(0, 2)
print(f"Computer chose: {computer}")

if user not in [0, 1, 2]:
    print("Entered invalid number, try again!")
else:
    if user == computer:
        print("It's a draw!")
    elif user == 0 and computer == 2:
        print("You win! Rock smashes Scissors.")
    elif user == 0 and computer == 1:
        print("You lose! Paper covers Rock.")
    elif user == 1 and computer == 0:
        print("You win! Paper covers Rock.")
    elif user == 1 and computer == 2:
        print("You lose! Scissors cut Paper.")
    elif user == 2 and computer == 1:
        print("You win! Scissors cut Paper.")
    elif user == 2 and computer == 0:
        print("You lose! Rock smashes Scissors.")
