
import tkinter as tk
import random
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Rock Paper Scissors")

# create labels
user_choice_label = tk.Label(root, text="Choose your move:")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer's move:")
computer_choice_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# create images for choices
rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((100,100)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((100,100)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((100,100)))

# create buttons
rock_button = tk.Button(root, text="Rock", image=rock_img, compound="top", width=100)
rock_button.pack(side="left")

paper_button = tk.Button(root, text="Paper", image=paper_img, compound="top", width=100)
paper_button.pack(side="left")

scissors_button = tk.Button(root, text="Scissors", image=scissors_img, compound="top", width=100)
scissors_button.pack(side="left")

# define game logic
def play_game(user_choice):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    # display computer's choice
    computer_choice_label.config(text="Computer's move: " + computer_choice)

    # determine winner
    if user_choice == computer_choice:
        result_label.config(text="Tie!")
    elif user_choice == 'Rock' and computer_choice == 'Scissors':
        result_label.config(text="You win!")
    elif user_choice == 'Paper' and computer_choice == 'Rock':
        result_label.config(text="You win!")
    elif user_choice == 'Scissors' and computer_choice == 'Paper':
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")

# bind buttons to game logic
rock_button.config(command=lambda: play_game('Rock'))
paper_button.config(command=lambda: play_game('Paper'))
scissors_button.config(command=lambda: play_game('Scissors'))

root.mainloop()
