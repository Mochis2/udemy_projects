from tkinter import *
from tkinter import messagebox
from tkinter import ttk 
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_list = [choice(letters) for char in range(randint(10, 12))]

    password_list += [choice(symbols) for char in range(randint(3, 4))]

    password_list += [choice(numbers) for char in range(randint(3, 4))]

    shuffle(password_list)

    gen_password = "".join(password_list)
    entry_password.insert(0, gen_password)
    pyperclip.copy(gen_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email = entry_email.get()
    website = entry_website.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password

        }
    }

    if email == '' or website == '' or password == '':
        messagebox.showerror(title='GitGud', message='You have to enter something everywhere dumbass.')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open('./data.json', mode='r') as file:
                    #Reading old data
                    data = json.load(file)

            except FileNotFoundError:
                with open('./data.json', mode='w') as file:
                    json.dump(new_data, file, indent=3)

            else:
                #Updating old data with new data
                data.update(new_data)

                with open('./data.json', mode='w') as file:
                    #Saving updated data
                    json.dump(data, file, indent=3)
                
            finally:
                entry_password.delete(0, END)
                entry_website.delete(0, END)
                
# ---------------------------- FIND PASSWORD ------------------------------- #

def search_website():
    website = entry_website.get()
    try:
        with open('./data.json', mode='r') as file:
            data = json.load(file)
            dict_email_and_pw = data[website]

    except (KeyError, FileNotFoundError):
        messagebox.showerror(title='GitGud', message=f'You either dont have "{website}" in the Password-Manager \nor you dont have any passwords at all, idiot!')
      
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f'Email: {dict_email_and_pw["email"]} \nPassword: {dict_email_and_pw["password"]} \n\nThe Password has been copied! Neat right?')
            pyperclip.copy(dict_email_and_pw["password"])

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Passwörter")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='./logo.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

#Labels
website_label = ttk.Label(window, text='Website:')
website_label.grid(column=0, row=1)

email_label = ttk.Label(window, text='Email/Username: ')
email_label.grid(column=0, row=2)

password_label = ttk.Label(window, text='Password:')
password_label.grid(column=0, row=3)

#Entries
entry_website = ttk.Entry(window, width=34)
entry_website.grid(column=1, row=1)
entry_website.focus()


entry_email = ttk.Entry(window, width=59)
entry_email.insert(0, 'maurice.eberhard@onify.ch')
entry_email.grid(column=1, row=2, columnspan=2)


entry_password = ttk.Entry(window, width=34, show='*')
entry_password.grid(column=1, row=3, ipadx=1)



search_button = ttk.Button(window, text='Search', width=23, command=search_website)
search_button.grid(column=2, row=1)

generate_button = ttk.Button(window, text='Generate Password', width=23, command=generate_password, takefocus=False)
generate_button.grid(column=2, row=3, sticky="w")

add_button = ttk.Button(window, text='Add', width=59, command=save, takefocus=False)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()