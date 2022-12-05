from tkinter import *


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=200, height=100)
window.config(padx=50, pady=50)


# Label
equal_label = Label(text="=",font=("Arial", 12, "normal"))
equal_label.grid(column=3, row=1)
equal_label.config(padx=10, pady=10)

m_label = Label(text="Miles", font=("Arial", 12, "normal"))
m_label.grid(column=2, row=1)

km_label = Label(text="Km", font=("Arial", 12, "normal"))
km_label.grid(column=5, row=1)

conversion_label = Label(text="0", font=("Arial", 12, "normal"))
conversion_label.grid(column=4, row=1)
conversion_label.config(padx=10, pady=10)

# Entry

input = Entry(width=10) 
print(input.get())
input.grid(column=1, row=1)

#Button

def button_clicked():
    try:
        result = round((int(input.get()) * 1.609), 2)
    except ValueError:
        result = "Error NaN"
    conversion_label.config(text=str(result))
    return result

button = Button(text="Calculate", command=button_clicked)
button.grid(column=5, row=1)



window.mainloop()


