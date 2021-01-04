from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x370")
root.resizable(False, False)
root.config(background= "#C0D6E4")

dictionary_selection = {1:"rock", 2:"paper", 3:"scissors"}


# interface
Label(root, text = "Choose Rock, Paper, Scissors", font="arial 16 bold", background = "#C0D6E4").place(x=50, y=10)

button_rock = Button(root, text="ROCK", width =8, height=2, font="arial 16 bold", command = lambda: play(1))
button_rock.place(x=50, y=50)
button_paper = Button(root, text="PAPER", width =8, height=2, font="arial 16 bold", command = lambda: play(2))
button_paper.place(x=200, y=50)
button_scissors = Button(root, text="SCISSORS", width =8, height=2, font="arial 16 bold", command = lambda: play(3))
button_scissors.place(x=350, y=50)
button_reset = Button(root, text="RESET", width =8, height=2, font="arial 16 bold", bg="green", command = lambda:reset())
button_reset.place(x=50, y=220)
button_exit = Button(root, text="EXIT", width =8, height=2, font="arial 16 bold", bg="red", command = lambda:exit())
button_exit.place(x=200, y=220)
result = Label(root, text = "Start Playing!", font="arial 16 bold", background = "#C0D6E4")
result.place(x=50, y=150)

# 1: rock 2: paper 3:scissors
def play(user_selection):
    cpu_random = random.randint(1, 3)
    print(cpu_random)
    if user_selection==cpu_random:
        result.config(text =f"Tie, you both selected {dictionary_selection[user_selection]}")
    elif user_selection == 1 and cpu_random == 2:
        result.config(text = f"You lost!, User: {dictionary_selection[user_selection]}, Computer: {dictionary_selection[cpu_random]}")
    elif user_selection == 1 and cpu_random == 3:
        result.config(text=f"You win!, User: {dictionary_selection[user_selection]}, Computer: {dictionary_selection[cpu_random]}")
    elif user_selection == 2 and cpu_random == 1:
        result.config(text=f"You win!, User: {dictionary_selection[user_selection]}, Computer: {dictionary_selection[cpu_random]}")
    elif user_selection == 2 and cpu_random == 3:
        result.config(text=f"You lost!, User: {dictionary_selection[user_selection]}, Computer: {dictionary_selection[cpu_random]}")
    elif user_selection == 3 and cpu_random == 1:
        result.config(text=f"You lost!, User: {dictionary_selection[user_selection]}, Computer: {dictionary_selection[cpu_random]}")
    elif user_selection == 3 and cpu_random == 2:
        result.config(text=f"You win!, User: {dictionary_selection[user_selection]}, Computer: {dictionary_selection[cpu_random]}")
    else:
        result.config(text="ERROR!")

def reset():
    result.config(text="Start Playing!")
def exit():
    root.destroy()



root.mainloop()

