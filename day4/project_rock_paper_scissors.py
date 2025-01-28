import random
from project_modules import check_game_logic

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
result = check_game_logic(sanitized_computer, sanitized_input)

print("Computer | You")
print("-----------------")
print(sanitized_computer, sanitized_input)
print(result)


