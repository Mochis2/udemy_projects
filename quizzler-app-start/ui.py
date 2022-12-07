from tkinter import *
from tkinter import ttk
from quiz_brain import QuizBrain



THEME_COLOR = "#375362"


class QuizInterface: 

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_label.grid(row=1, column=2, columnspan=2)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="TEST", fill=THEME_COLOR, width=280, font=("Arial", 15, "italic"))
        self.canvas.grid(row=2, column=1, columnspan=2, pady=40)

        button_img_true = PhotoImage(file="./images/true.png")
        self.button_true = ttk.Button(image=button_img_true, takefocus=False, command=self.question_is_right)
        self.button_true.grid(row=3, column=1)

        button_img_false = PhotoImage(file="./images/false.png")
        self.button_false = ttk.Button(image=button_img_false, takefocus=False, command=self.question_is_wrong)
        self.button_false.grid(row=3, column=2)
        
        self.get_next_question()

        self.window.mainloop()

    def question_is_right(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def question_is_wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="QUIZ HAS ENDED! HURRAY!")
            self.button_true.configure(state="disabled")
            self.button_false.configure(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="#4ea85f")
        else: 
            self.canvas.configure(bg="#a84e4f")
        self.window.after(1000, self.get_next_question)
            