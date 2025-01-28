
# function to check rock paper scissors game
def check_game_logic(sanitized_computer, sanitized_input):
    """
    Check game logic of rock paper scissors
    """
    if sanitized_computer == "rock" and sanitized_input == "paper":
        return "You Win!"
    elif sanitized_computer == "rock" and sanitized_input == "scissors":
        return "You lose!"
    elif sanitized_computer == "rock" and sanitized_input == "rock":
        return "Draw!"
    elif sanitized_computer == "paper" and sanitized_input == "paper":
        return "Draw!"
    elif sanitized_computer == "paper" and sanitized_input == "rock":
        return "You Lose"
    elif sanitized_computer == "paper" and sanitized_input == "scissors":
        return "You Win!"
    elif sanitized_computer == "scissors" and sanitized_input == "scissors":
        return "Draw"
    elif sanitized_computer == "scissors" and sanitized_input == "rock":
        return "You Win"
    elif sanitized_computer == "scissors" and sanitized_input == "paper":
        return "You Lose"
