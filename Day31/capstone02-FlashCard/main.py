from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn={}
current_card={}

try:
    data=pd.read_csv("data/words_to_learn.csv")
except:
    original_data=pd.read_csv("data/french_words.csv")
    to_learn= original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card= random.choice(to_learn)
    canvas.itemconfigure(title, text="French", fill="black")
    canvas.itemconfigure(word, text=current_card["French"], fill="black")
    canvas.itemconfigure(card, image=card_front)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_card
    canvas.itemconfigure(card, image=card_back)
    canvas.itemconfigure(title, text="English", fill="white")
    canvas.itemconfigure(word, text=current_card["English"], fill="white")

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data= pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



window = Tk()
window.title("Flash Cards")

flip_timer= window.after(3000, func=flip_card)

window.config(bg=BACKGROUND_COLOR)
window.config(padx=50,pady=50)

canvas = Canvas(height=526, width=800, highlightthickness=0)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
card=canvas.create_image(400,263,image=card_front)
title = canvas.create_text(400,120, text="Title", font=("Arial", 40, "italic"))
word = canvas.create_text(400,263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

cross_image= PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1,column=0)

right_image= PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(row=1,column=1)

next_card()







window.mainloop()

