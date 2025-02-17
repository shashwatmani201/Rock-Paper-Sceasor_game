import random
computerchoice= random.choice([1,2,3])
choice=input("ENTER FOR: \n ROCK=   R\n PAPER=  P\n SCISSORS=S\n").lower()
choicedict= {"r":1,"p":2,"s":3}
revchoice={1:"ROCK",2:"PAPER",3:"SCEASOR"}
userchoice=choicedict[choice]
if(computerchoice==userchoice):
    print("MATCH IS DRAW")
elif(((computerchoice-userchoice)==1 )or((computerchoice-userchoice)==-2)):
    print("OOPS!! COMPUTER WINS")
else:
    print("CONGRATULATIONS!! YOU WON" )

# # CONDITION OF COPUTER WIN
# # 2-1 = 1
# # 1-3 =-2   
# # 3-2 = 1
'''
import random
import tkinter as tk
from tkinter import messagebox

# Function to play the game
def play_game(user_choice):
    choices = {1: "ROCK", 2: "PAPER", 3: "SCISSORS"}
    computer_choice = random.choice([1, 2, 3])
    
    # Determine winner
    if computer_choice == user_choice:
        result_text = "MATCH IS DRAW!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        result_text = "CONGRATULATIONS!! YOU WON 🎉"
    else:
        result_text = "OOPS!! COMPUTER WINS 😢"
    
    # Update labels
    user_label.config(text=f"Your Choice: {choices[user_choice]}")
    comp_label.config(text=f"Computer's Choice: {choices[computer_choice]}")
    result_label.config(text=result_text)

# Creating the GUI window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0", fg="blue")
title_label.pack(pady=10)

# Labels to show choices
user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 14), bg="#f0f0f0")
user_label.pack()
comp_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 14), bg="#f0f0f0")
comp_label.pack()
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="red", bg="#f0f0f0")
result_label.pack(pady=10)

# Buttons for user choice
rock_btn = tk.Button(root, text="Rock 🪨", font=("Arial", 12), width=10, command=lambda: play_game(1))
rock_btn.pack(pady=5)

paper_btn = tk.Button(root, text="Paper 📄", font=("Arial", 12), width=10, command=lambda: play_game(2))
paper_btn.pack(pady=5)

scissors_btn = tk.Button(root, text="Scissors ✂️", font=("Arial", 12), width=10, command=lambda: play_game(3))
scissors_btn.pack(pady=5)

# Run the application
root.mainloop()'''