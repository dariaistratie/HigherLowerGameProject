from art import logo, vs
import random
from game_data import data


def get_random_person():
    """Select a random person from the dataset."""
    return random.choice(data)


def display_comparison(person_a, person_b):
    """Display the comparison between the two people, including 'vs' between them."""
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
    print(vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")


def play_game():
    """The main function of the game."""
    while True:
        print(logo)
        score = 0
        person_b = get_random_person()

        while True:
            person_a = person_b
            person_b = get_random_person()

            while person_a == person_b:
                person_b = get_random_person()

            display_comparison(person_a, person_b)
            user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

            if person_a['follower_count'] > person_b['follower_count']:
                correct_answer = 'A'
            else:
                correct_answer = 'B'

            if user_choice == correct_answer:
                score += 1
                print(f"Correct! Your score is now: {score}\n")
            else:
                print(f"Wrong! Final score: {score}")
                break  # Stop the game if the user makes a mistake

        # Ask if the user wants to play again
        if input("Do you want to play again? (Y/N): ").upper() != 'Y':
            print("Thanks for playing!")
            break


# Run the game
play_game()
