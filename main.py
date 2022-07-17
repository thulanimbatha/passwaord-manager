from email.mime import image
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    # get entry values 
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# add label - website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# add Entry - website entry, width 51
website_entry = Entry(width=51)
website_entry.focus()   # insert cursor
website_entry.grid(column=1, row=1, columnspan=2)

# add label - Email/username
website_label = Label(text="Email/Username:")
website_label.grid(column=0, row=2)

# add Entry - email/username entry, width 51
email_username_entry = Entry(width=51)
email_username_entry.insert(0, "youarenothing@underachiever.com")   # insert default email text
email_username_entry.grid(column=1, row=2, columnspan=2)

# add label - password
website_label = Label(text="Password:")
website_label.grid(column=0, row=3)

# add entry - password, width 33
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# add Button - generate password
gen_password_button = Button(text="Generate Password")
gen_password_button.grid(column=2, row=3)

# add Button - add, width 43
add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()