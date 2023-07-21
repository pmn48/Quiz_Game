from tkinter import *
from PIL import ImageTk, Image
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
FONT2 = ("Arial", 12, "normal")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Questions go here", fill=THEME_COLOR, width=250,
                                                     font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = ImageTk.PhotoImage(Image.open("images/true.png"))
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_click)
        self.true_button.grid(row=2, column=0)

        false_image = ImageTk.PhotoImage(Image.open("images/false.png"))
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_click)
        self.false_button.grid(row=2, column=1)

        self.score_lab = Label(text=f"Score: {self.quiz.score}", background=THEME_COLOR, foreground="white", font=FONT2)
        self.score_lab.grid(column=1, row=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have completed all questions! Your final score is {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_click(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_click(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct: bool):
        if is_correct:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, func=self.display_next)

    def display_next(self):
        self.score_lab.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(background="white")
        self.get_next_question()
