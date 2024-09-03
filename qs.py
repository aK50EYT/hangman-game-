import random
import string
from data import data
import tkinter as tk
from tkinter import messagebox


def get_valid_word(data):
    word = random.choice(data)
    while '_' in word or ' ' in word:
        word = random.choice(data)
    return word


class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word = get_valid_word(data)
        self.word_letters = set(self.word)  # Letters in the word
        self.alphabet = set(string.ascii_lowercase)
        self.used_letters = set()  # Letters the user has guessed

        # GUI components
        self.label_used_letters = tk.Label(root, text="Used Letters: ")
        self.label_used_letters.pack()

        self.label_word = tk.Label(root, text="Current Word: " + " ".join('_' * len(self.word)))
        self.label_word.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button_guess = tk.Button(root, text="Guess", command=self.guess_letter)
        self.button_guess.pack()

        self.label_message = tk.Label(root, text="")
        self.label_message.pack()

    def guess_letter(self):
        user_letter = self.entry.get().lower()
        self.entry.delete(0, tk.END)  # Clear the entry after getting the input

        if user_letter in self.alphabet - self.used_letters:
            self.used_letters.add(user_letter)

            if user_letter in self.word_letters:
                self.word_letters.remove(user_letter)
                self.update_word_display()

                if len(self.word_letters) == 0:
                    messagebox.showinfo("Congratulations!", f"You've guessed the word: {self.word}")
                    self.reset_game()
            else:
                self.label_message.config(text="Wrong guess!")

        elif user_letter in self.used_letters:
            self.label_message.config(text="You have already used that letter.")
        else:
            self.label_message.config(text="Invalid character. Please try again.")

        self.update_used_letters_display()

    def update_word_display(self):
        word_list = [letter if letter in self.used_letters else '_' for letter in self.word]
        self.label_word.config(text="Current Word: " + " ".join(word_list))

    def update_used_letters_display(self):
        self.label_used_letters.config(text="Used Letters: " + " ".join(sorted(self.used_letters)))

    def reset_game(self):
        self.word = get_valid_word(data)
        self.word_letters = set(self.word)
        self.used_letters = set()
        self.update_word_display()
        self.update_used_letters_display()
        self.label_message.config(text="")


# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
