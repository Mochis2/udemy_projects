from tkinter import *
from tkinter import ttk
import requests
import random

def get_quote():
    response = requests.get(url="https://api.whatdoestrumpthink.com/api/v1/quotes/random")
    response.raise_for_status()
    data = response.json()
    random_quote = data["message"]
    canvas.itemconfig(quote_text, text=random_quote)

def get_message():
    list_with_names = ['Alex', 'Fabian', 'Jochen', 'Darragh', 'Maurice']
    response = requests.get(url="https://api.whatdoestrumpthink.com/api/v1/quotes")
    response.raise_for_status()
    data = response.json()
    random_message = random.choice(data["messages"]["personalized"])
    random_name = random.choice(list_with_names)
    canvas.itemconfig(quote_text, text=f'{random_name} {random_message}')

     
def random_function():
    number = random.randint(1,2)
    if number == 1:
        get_message()
    if number == 2:
        get_quote()


window = Tk()
window.title("Trump Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="./background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Trump Quote Goes HERE", width=250, font=("Arial", 15, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="./trump.png")
kanye_button = ttk.Button(image=kanye_img, command=random_function, takefocus=False)
kanye_button.grid(row=1, column=0)


window.mainloop()