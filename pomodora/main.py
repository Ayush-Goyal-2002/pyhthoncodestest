
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    countdown(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    count_min = math.floor(count/60)
    count_sec = count%60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0 :
        window.after(1000, countdown, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("PAMADORA")
window.config(padx=100, pady=100, bg=YELLOW , highlightthickness=0)



title_label = Label(text="TIMER", fg= GREEN, font=(FONT_NAME, 50),  bg=YELLOW )
title_label.grid(column=1, row=0)

canvas= Canvas(width=200, height=224, bg= YELLOW)
tamoto_png= PhotoImage(file= "tomato.png")
canvas.create_image(100,112 ,image=tamoto_png)
timer_text = canvas.create_text(100,130, text = "00:00", fill="white", font=(FONT_NAME,35,"bold"))


start_button= Button(text="Start", highlightthickness=0, command=start_timer )
start_button.grid(column=0, row=2)
reset_button= Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg= GREEN, bg= YELLOW)
check_marks.grid()

canvas.grid(column=1, row= 1)





window.mainloop()