import random

def generate_number():
    return str(random.randint(1000, 9999))

def get_user_input():
    while True:
        user_input = input("Guess the 4-digit number: ")
        if user_input.isdigit() and len(user_input) == 4:
            return user_input
        print("Invalid input! Please enter a 4-digit number.")

def evaluate_guess(guess, secret):
    correct_positions = sum(1 for g, s in zip(guess, secret) if g == s)
    correct_digits = sum(min(guess.count(d), secret.count(d)) for d in set(secret))
    misplaced_digits = correct_digits - correct_positions
    return correct_positions, misplaced_digits

def play_game():
    secret_number = generate_number()
    attempts = 0
    
    print("Welcome to the Number Guessing Game! Try to guess the 4-digit number.")
    while True:
        guess = get_user_input()
        attempts += 1

        if guess == secret_number:
            print(f"\n Congratulations! You guessed the number {secret_number} in {attempts} attempts! ")
            break
        
        correct_positions, misplaced_digits = evaluate_guess(guess, secret_number)
        print(f"correctly placed digits: {correct_positions}")
        print(f"Misplaced but correct digits: {misplaced_digits}\n")

    return attempts

def main():
    while True:
        attempts = play_game()
        play_again = input("\nWant to play again? (yes/no): ").strip().lower()
        if play_again not in ('yes', 'y'):
            print(f"Thanks for playing! Your best attempt was {attempts} tries.")
            break

if __name__ == "__main__":
    main()
