from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
random_dict = {}
try:
    data_file = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    data = original_data.to_dict(orient="records")
else:
    data = data_file.to_dict(orient="records")


# ---------------------------- WORD CREATION ------------------------------- #
def pick_word():
    global random_dict, flip_timer
    window.after_cancel(flip_timer)
    random_dict = random.choice(data)
    word_picked = random_dict["French"]
    canvas.itemconfig(image_box, image=front_page)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=word_picked, fill="black")
    flip_timer = flip_timer = window.after(3000, word_meaning)


# ---------------------------- WORD MEANING MECHANISM ------------------------------- #
def word_meaning():
    canvas.itemconfig(image_box, image=back_page)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=f"{random_dict['English']}", fill="white")


# ---------------------------- SAVING WORDS TO LEARN MECHANISM ------------------------------- #
def remove_to_learn():
    data.remove(random_dict)
    words_to_learn = pd.DataFrame(data)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    pick_word()


# ---------------------------- UI SETUP ------------------------------ #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, word_meaning)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_page = PhotoImage(file="./images/card_front.png")
back_page = PhotoImage(file="./images/card_back.png")
image_box = canvas.create_image(400, 261, image=front_page)
language = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
time = canvas.create_text(750, 50, text="", fill="#890F0D", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, padx=50, pady=50, command=pick_word)
wrong_button.grid(row=1, column=0)
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0,
                      padx=50, pady=50, command=remove_to_learn)
right_button.grid(row=1, column=1)

pick_word()

window.mainloop()
