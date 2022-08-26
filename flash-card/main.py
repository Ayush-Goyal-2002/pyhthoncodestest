from tkinter import *
import csv
import pandas

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    print("h")








BACKGROUND_COLOR = "#B1DDC6"
window= Tk()
window.config(padx=50,pady=50,background= BACKGROUND_COLOR)
window.title("Flash Card")

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image= wrong_img,background=BACKGROUND_COLOR, command=next_card())
wrong_button.grid(row=1, column=0)
right_img = PhotoImage(file="images/right.png")
right_button = Button(image= right_img,background=BACKGROUND_COLOR,command=next_card())
right_button.grid(row=1, column=1)




canvas = Canvas(width = 800, height =526)
canvas.grid(row=0, column=0, columnspan=2)
card_front = PhotoImage(file="images/card_front.png")
card_back= PhotoImage(file="images/card_back.png")

canvas.create_image(400,263, image=card_front )
canvas.grid(row=0,column=0)
canvas.config(highlightthickness=0,background=BACKGROUND_COLOR)
canvas.create_text(400,150,text="Title", font=("Arial", 48, "italic"))
canvas.create_text(400, 256,text="Word", font=("Arial", 24, "italic"))























window.mainloop()