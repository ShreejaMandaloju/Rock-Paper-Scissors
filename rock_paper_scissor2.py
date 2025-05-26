import random

def get_user_choice():
    choice = input("Enter Rock, Paper, or Scissors: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Try again.")
        choice = input("Enter Rock, Paper, or Scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
        (user == 'scissors' and computer == 'paper') or \
        (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    playing = True

    while playing:
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"👩 You chose: {user}")
        print(f"💻 Computer chose: {computer}")
        print(determine_winner(user, computer))

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            playing = False
            print("Thanks for playing! 👋")

# Run the game
if __name__ == "__main__":
    play_game()
