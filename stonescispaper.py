from tkinter import *
import random

window = Tk()

window.geometry("800x400")
window.title("ROCK PAPER SCISSORS")

frame = Frame(window)
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

name = Label(frame, text="Rock Paper Scissors-Player vs Computer", font=100)
name.place(x=250, y=20)

Label1 = Label(frame, text="Player", font="normal 15")

Label2 = Label(frame, text="VS", font="normal 15")

Label3 = Label(frame, text="Computer", font="normal 15")

Label1.place(x=80, y=50, width=100)
Label2.place(x=350, y=50, width=100)
Label3.place(x=600, y=50, width=100)

rock_png = PhotoImage(file="rock.png")
scissors_png = PhotoImage(file="scissors.png")
paper_png = PhotoImage(file="paper.png")

user_image = Label(frame, image="")
user_image.place(x=80, y=100)

comp_image = Label(frame, image="")
comp_image.place(x=600, y=100)

Label4 = Label(
    frame, text="", font="normal 20", width=15, borderwidth=2, relief="solid"
)
Label4.place(x=275, y=250)


def Rock():
    user = "Rock"
    computer = random.choice(["Rock", "Paper", "Scissors"])
    user_image.config(image=rock_png)
    if user == computer:
        Label4.config(text="Tie")
        comp_image.config(image=rock_png)
    elif computer == "Paper":
        Label4.config(text="Computer Wins !")
        comp_image.config(image=paper_png)

    else:
        Label4.config(text="U WIN !")
        comp_image.config(image=scissors_png)


b1 = Button(frame, text="Rock", font="10", width=20, command=Rock)
b1.place(x=100, y=300)


def Paper():
    user = "Paper"
    computer = random.choice(["Rock", "Paper", "Scissors"])
    user_image.config(image=paper_png)
    if user == computer:
        Label4.config(text="Tie")
        comp_image.config(image=paper_png)
    elif computer == "Scissors":
        Label4.config(text="Computer Wins !")
        comp_image.config(image=scissors_png)

    else:
        Label4.config(text="U WIN !")
        comp_image.config(image=rock_png)


b2 = Button(frame, text="Paper", font="10", width=20, command=Paper)
b2.place(x=300, y=300)


def Scissors():
    user = "Scissors"
    computer = random.choice(["Rock", "Paper", "Scissors"])
    user_image.config(image=scissors_png)
    if user == computer:
        Label4.config(text="Tie")
        comp_image.config(image=scissors_png)
    elif computer == "Rock":
        Label4.config(text="Computer Wins !")
        comp_image.config(image=rock_png)

    else:
        Label4.config(text="U WIN !")
        comp_image.config(image=paper_png)


b3 = Button(frame, text="Scissors", font="10", width=20, command=Scissors)
b3.place(x=500, y=300)


window.mainloop()
