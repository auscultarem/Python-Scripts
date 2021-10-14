from tkinter import *
import pandas as pd
import random



# ---------------------------- Global------------------------------- #
WHITE = "#FDFEFF"
BACKGROUND_COLOR = "#B1DDC6"
data = pd.read_csv("./data/french_words.csv")
data_dict = data.to_dict()
random_choice = 0


# ----------------------------Change Word------------------------------- #
def change_word():
    global random_choice, flip_timer
    window.after_cancel(flip_timer)
    random_choice = random.randint(0, len(data))
    english_word = data_dict["English"][random_choice]
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=f"{english_word}", fill="black")
    canvas.itemconfig(background, image=image_front)
    flip_timer = window.after(3000, func=flip_card)


# ----------------------------Change Word------------------------------- #
def flip_card():
    global random_choice

    spanish_word = data_dict["Spanish"][random_choice]
    canvas.itemconfig(card_title, text="Español", fill="white")
    canvas.itemconfig(card_word, text=f"{spanish_word}", fill="white")
    canvas.itemconfig(background, image=image_back)



#------------------User Interface --------------------------#
window = Tk()
window.title("Flash Card Apply")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
image_front = PhotoImage(file="./images/card_front.png")
image_back = PhotoImage(file="./images/card_back.png")

background = canvas.create_image(400, 263, image=image_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 20, "italic"))
card_word = canvas.create_text(400, 250, text="", font=("Arial", 30, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
bad_button = Button(image=wrong_image,highlightthickness=0,command=change_word)
bad_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=change_word)
right_button.grid(column=1, row=1)

change_word()
window.mainloop()
