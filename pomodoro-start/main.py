from tkinter import *
from tkinter.ttk import *
import math
from plyer import notification
import sys, os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 
SHORT_BREAK_MIN = 5 
LONG_BREAK_MIN = 20 
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        timer_label.config(text="WORKING TIME!😍")
        style.configure("BW.TLabel", foreground=GREEN)
        work_noti()
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="LONG BREAK!😴")
        style.configure("BW.TLabel", foreground=RED)
        long_break_noti()
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        timer_label.config(text="QUICK BREAK!😪")
        style.configure("BW.TLabel", foreground=PINK)
        break_noti()



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        for sec in range(count_sec):
            count_sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔️"
        checkmark_label.config(text=mark)

# ---------------------------- FILEPATH.EXE ------------------------------- #

filepath = os.path.dirname(os.path.realpath(__file__)) + r"\tomato.png"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Technique")
window.config(padx=100, pady=50, bg=YELLOW)
style = Style()




style.configure("BW.TLabel", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label = Label(text="Timer", style="BW.TLabel")
timer_label.grid(column=2, row=1)

checkmark_label = Label(text="", background=YELLOW, foreground=GREEN ,font=(FONT_NAME, 13, "bold"))
checkmark_label.grid(column=2, row=4)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=filepath)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=2, row=2)



style.configure("TButton", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 13, "bold"))
start_button = Button(text="Start", command=start_timer, style="TButton", takefocus=False)
start_button.grid(column=1, row=3)
end_button = Button(text="Reset",style="TButton", command=reset_timer, takefocus=False)
end_button.grid(column=3, row=3)



# ---------------------------- NOTIFICATION ------------------------------- #

def break_noti():
    notification.notify(
        title = 'BREAK TIME 🧘',
        message = 'We chillin',
        app_icon = None,
        timeout = 10,
    )

def work_noti():
    notification.notify(
        title = 'WORKING TIME ✍️',
        message = 'You need to work, lazy ass.',
        app_icon = None,
        timeout = 10,
    )

def long_break_noti():
    notification.notify(
        title = 'LONG BREAK 🛌',
        message = 'We chillin longer',
        app_icon = None,
        timeout = 10,
    )




window.mainloop()

















