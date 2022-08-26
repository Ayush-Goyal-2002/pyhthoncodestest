from tkinter import *
class QuizInterface:
    def __init__(self,quiz_brain: ):
        self.quiz = quiz_brain
        self.window =Tk()
        self.window.title("Quizzer")
        self.window.config(pady=20,padx=20,bg="BLACK")
        self.score_label = Label(text="score : 0", bg="Black", fg="White")
        self.score_label.grid(row=0,column=1)


        self.canvas =Canvas(height=250, width=300,bg = "white")

        self.question_text = self.canvas.create_text(text="question comes here", fill= "black", font=("Arial "))

        self.canvas.grid(row=1, column=0, columnspan=2)

        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        self.true_button = Button(image=true_img)
        set.false_image = Button(image=false_img)

        self.window.mainloop()


        def get_next_question(self):
            self.quiz.next_question

