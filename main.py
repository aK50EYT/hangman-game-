import random
import string
from data import data
def get_valid_word(data):
    word = random.choice(data)
    while '_' in word or ' ' in word:
        word = random.choice(data)
    return word


def hangman():
    word = get_valid_word(data)
    word_litters = set(word)  # Letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set()  # Letters the user has guessed

    while len(word_litters) > 0:
        # Display used letters
        print("You have used these letters: ", " ".join(sorted(used_letters)))

        # Display current state of the word
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", " ".join(word_list))

        # Get input from the user
        user_letter = input("Guess a letter: ")

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
        if user_letter in word_litters:
            word_litters.remove(user_letter)
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please try again.")
    print("Current word: "," ".join(word_list))
    print(f"Congratulations! You've guessed the word: {word}")
    print("tttt")


hangman()
