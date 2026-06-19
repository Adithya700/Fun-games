import random

choices = {
    'rock': '✊',
    'paper': '✋',
    'scissors': '✌️'
}

player_score = 0
computer_score = 0
rounds_played = 0
max_rounds = 5

print("Welcome to Rock-Paper-Scissors! Best of 5 matches.\n")

while rounds_played < max_rounds:
    user_input = input("Enter your choice (rock/paper/scissors): ").lower()
    if user_input not in choices:
        print("Invalid choice, please try again.\n")
        continue
    
    computer_choice = random.choice(list(choices.keys()))
    print(f"You chose {choices[user_input]} {user_input.capitalize()}")
    print(f"Computer chose {choices[computer_choice]} {computer_choice.capitalize()}")
    
    if user_input == computer_choice:
        print("It's a tie!\n")
    elif (user_input == 'rock' and computer_choice == 'scissors') or \
         (user_input == 'scissors' and computer_choice == 'paper') or \
         (user_input == 'paper' and computer_choice == 'rock'):
        print("You win this round!\n")
        player_score += 1
    else:
        print("Computer wins this round!\n")
        computer_score += 1
    
    rounds_played += 1
    print(f"Score: You {player_score} - {computer_score} Computer\n")

print("Game over!")
if player_score > computer_score:
    print("🎉 You won the match!")
elif computer_score > player_score:
    print("💻 Computer won the match!")
else:
    print("It's a draw!")