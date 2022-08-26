from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
canvas = Canvas(width=220, height=220)
window.config(pady=20 , padx= 20)
icon_png = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image=icon_png)
# icon_png.grid(row=0, column = 1)

website = Label(text="Website")
email = Label(text="Email/Username")
password = Label(text="Password")
website.grid(row=1, column=0)
email.grid(row=2, column=0)
password.grid(row=3, column=0)

gen_pass_button = Button(text="Generate Password")
add_button = Button(text="Add")
gen_pass_button.grid(row= 3, column=2)
add_button.grid(row=4, column=1)

website_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=19)
website_entry.grid(row=1, column=1,columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1)



canvas.grid(row=5, column=3)


















window.mainloop()