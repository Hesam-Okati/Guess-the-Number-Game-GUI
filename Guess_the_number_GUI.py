"""
Guess the Number Game (GUI Version with Tkinter)

This is a simple number guessing game where the user enters a guess, and 
the program gives hints if the guess is too high or too low until the correct number is guessed.

Modules Used:
- random: For generating a random number.
- tkinter: For creating the graphical user interface.

"""

import random
import tkinter as tk
from tkinter import messagebox

class GuessNumberGame:
    def __init__(self, root):
        """ Initialize the GUI components and start the game """
        self.root = root
        self.root.title("Guess the Number Game")
        self.root.geometry("400x300")

        # Generate a random number between 0 and 100
        self.computer_guess = random.randint(0, 100)

        # Create GUI elements
        self.label = tk.Label(root, text="Enter your guess (0-100):", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Arial", 12))
        self.submit_button.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game, font=("Arial", 12))
        self.reset_button.pack(pady=10)

    def check_guess(self):
        """ Check the user's guess and provide feedback """
        try:
            user_guess = int(self.entry.get())

            if user_guess < 0 or user_guess > 100:
                self.result_label.config(text="Please enter a number between 0 and 100!", fg="red")
                return

            if user_guess < self.computer_guess:
                self.result_label.config(text="Your number is too low! Try again.", fg="orange")
            elif user_guess > self.computer_guess:
                self.result_label.config(text="Your number is too high! Try again.", fg="orange")
            else:
                self.result_label.config(text="🎉 You win! 🎉", fg="green")
                messagebox.showinfo("Congratulations!", "You guessed the correct number!")

        except ValueError:
            self.result_label.config(text="Invalid input! Please enter a number.", fg="red")

    def reset_game(self):
        """ Reset the game by generating a new number and clearing input """
        self.computer_guess = random.randint(0, 100)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="Game reset! Enter a new guess.", fg="blue")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
