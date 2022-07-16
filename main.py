from email.mime import image
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# create Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
# use PhotoImage class with file name
logo_img = PhotoImage(file="logo.png")
# create image
canvas.create_image(100, 100, image=logo_img)
# canvas layout
canvas.pack()


window.mainloop()