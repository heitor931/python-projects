import random

options = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(options)
sanitized_computer = computer_choice.lower()
user_input = input("Choose Rock, paper or scissors: ")

# Sanitize user input
sanitized_input = user_input.lower()
# Check if user input is a valid input
while sanitized_input not in [o.lower() for o in options]:
  corrected_user = input("Not a Valid input, Valid are Rock, Paper, scissors: ")
  if corrected_user.lower() in [o.lower() for o in options]:
      sanitized_input = corrected_user.lower()
      break

# Check win/win logic
print("="* 16)
if sanitized_computer == "rock" and sanitized_input == "paper":
    print("You Win!")
elif sanitized_computer == "rock" and sanitized_input == "scissors":
    print("You lose!")
elif sanitized_computer == "rock" and sanitized_input == "rock":
    print("Draw!")
elif sanitized_computer == "paper" and sanitized_input == "paper":
    print("Draw!")
elif sanitized_computer == "paper" and sanitized_input == "rock":
    print("You Lose")
elif sanitized_computer == "paper" and sanitized_input == "scissors":
    print("You Win!")
elif sanitized_computer == "scissors" and sanitized_input == "scissors":
    print("Draw")
elif sanitized_computer == "scissors" and sanitized_input == "rock":
    print("You Win")
elif sanitized_computer == "scissors" and sanitized_input == "paper":
    print("You Lose")


print("Computer | You")
print("-----------------")
print(sanitized_computer, sanitized_input)


