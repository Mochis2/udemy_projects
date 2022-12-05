from tkinter import *
from tkinter import ttk
import os
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#---------------- FILEPATH ------------------


filepath_front_card = os.path.dirname(os.path.realpath(__file__)) + r"\images\card_front.png"
filepath_button_wrong = os.path.dirname(os.path.realpath(__file__)) + r"\images\wrong.png"
filepath_button_right = os.path.dirname(os.path.realpath(__file__)) + r"\images\right.png"
filepath_back_card = os.path.dirname(os.path.realpath(__file__)) + r"\images\card_back.png"
filepath_italian_words = os.path.dirname(os.path.realpath(__file__)) + r"\data\italian_words.csv"
filepath_arrow = os.path.dirname(os.path.realpath(__file__)) + r"\images\arrow.png"
filepath_data_known = os.path.dirname(os.path.realpath(__file__)) + r"\data\words_that_i_know.csv"
filepath_data_unknown = os.path.dirname(os.path.realpath(__file__)) + r"\data\words_to_learn.csv"


#---------------- DATA ------------------

data = pandas.read_csv(filepath_italian_words)
list_of_all_words = data.to_dict(orient="records")
current_card = {}
list_with_cards_known = []
list_with_cards_unknown = []


#---------------- CARD FUNCTIONS ------------------
def next_card():
    global current_card
    current_card = random.choice(list_of_all_words)
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_language, fill='black', text='Italian')
    canvas.itemconfig(card_word, fill='black', text=current_card['Italian'])

def flip_card():
    global current_card
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_language, fill='white', text='English')
    canvas.itemconfig(card_word, fill='white', text=current_card["English"])

def flip_card_back():
    global current_card
    canvas.itemconfig(card_img, image=card_front_img)
    canvas.itemconfig(card_language, fill='black', text='Italian')
    canvas.itemconfig(card_word, fill='black', text=current_card['Italian'])


def if_card_is_clicked(event):
    flip_card()


def delete_row_in_file():
    old_data = pandas.read_csv(filepath_italian_words)
    file_index = old_data.index[(old_data.Italian == current_card['Italian'])]
    old_data.drop(index=file_index, axis=0, inplace=True)
    old_data.to_csv(filepath_italian_words, index=False)


def if_right():
    global current_card
    global list_with_cards_known
    list_with_cards_known.append(current_card)
    new_data = pandas.DataFrame(list_with_cards_known)
    new_data.to_csv(filepath_data_known, index=False)
    delete_row_in_file()
    next_card()

def if_wrong():
    next_card()

#---------------- UI ------------------


window = Tk()
window.title('FlashcardApp')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file=filepath_front_card)
card_back_img = PhotoImage(file=filepath_back_card)
card_img = canvas.create_image(400, 263, image=card_front_img)
canvas.bind("<Button-1>", if_card_is_clicked)

card_language = canvas.create_text(400, 150, text="Italian", font=("Ariel", 35, "italic"))
card_word = canvas.create_text(400, 263, text='t', font=("Ariel", 55, "bold"))

canvas.grid(column=1, row=1, columnspan=3)

button_arrow_img = PhotoImage(file=filepath_arrow)
button_arrow = Button(image=button_arrow_img, highlightthickness=0, highlightcolor=BACKGROUND_COLOR, borderwidth=0, command=flip_card_back)
button_arrow.grid(column=2, row=2)

button_wrong_img = PhotoImage(file=filepath_button_wrong)
button_wrong = Button(image=button_wrong_img, highlightthickness=0, highlightcolor=BACKGROUND_COLOR, borderwidth=0, command=if_wrong)
button_wrong.grid(column=1, row=2)


button_right_img = PhotoImage(file=filepath_button_right)
button_right = Button(image=button_right_img, highlightcolor=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=if_right)
button_right.grid(column=3, row=2)


next_card()


window.mainloop()