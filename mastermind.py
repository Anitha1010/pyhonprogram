import random

def get_hint(secret_number, guess):
    correct_digits = sum(1 for s, g in zip(secret_number, guess) if s == g)
    return correct_digits

def play_round(setter, guesser, length):
    secret_number = setter()
    attempts = 0

    while True:
        attempts += 1
        guess = guesser(length)
        if guess == secret_number:
            print(f"Correct! The number was {secret_number}.")
            break
        hint = get_hint(secret_number, guess)
        print(f"Attempt {attempts}: {guess} -> {hint} correct digits.")
    
    return attempts

def player_set_number():
    return input("Player, set a multi-digit number: ")

def player_guess_number(length):
    return input(f"Player, guess a {length}-digit number: ")

def random_number(length):
    return "".join(random.choice("0123456789") for _ in range(length))

def mastermind_game():
    length = int(input("Enter the length of the number to guess: "))
    print("\nPlayer 1 sets the number.")
    attempts_player_2 = play_round(player_set_number, player_guess_number, length)

    
    print("\nPlayer 2 sets the number.")
    attempts_player_1 = play_round(player_set_number, player_guess_number, length)


    
    if attempts_player_1 < attempts_player_2:
        print("\nPlayer 1 wins and is crowned Mastermind!")
    elif attempts_player_2 < attempts_player_1:
        print("\nPlayer 2 wins and is crowned Mastermind!")
    else:
        print("\nIt's a tie!")

if __name__ == "__main__":
    mastermind_game()
