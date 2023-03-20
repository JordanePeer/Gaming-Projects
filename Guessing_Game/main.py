import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guessing Game")

        # generate a random number
        self.answer = random.randint(1, 100)

        # create widgets
        self.prompt_label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.prompt_label.pack()

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_guess)
        self.submit_button.pack()

    def check_guess(self):
        # get user's guess
        guess = int(self.guess_entry.get())

        # compare guess to answer
        if guess == self.answer:
            messagebox.showinfo("Correct!", "You guessed the correct number!")
        elif guess > self.answer:
            messagebox.showwarning("Incorrect", "Too high! Guess again.")
        else:
            messagebox.showwarning("Incorrect", "Too low! Guess again.")
        
        # clear the guess entry
        self.guess_entry.delete(0, tk.END)

# create the GUI
root = tk.Tk()
game = GuessingGame(root)
root.mainloop()