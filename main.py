from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    #Password Generator Project - Imported from previous Day 5 project modified to have no user inputs

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # list comprehension
    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    # combine all 3 lists 
    password_list = password_letters + password_symbols + password_numbers
    # shuffle
    shuffle(password_list)
    
    password = "".join(password_list)

    # add password to the entry
    password_entry.insert(0, password)

    # copy to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    # get entry values 
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    # create json file
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    # check to see if entries don't have any values entered
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops!", message="Do not leave any fields empty")
    else:
        # displays message - user details are correct? RETURNS BOOLEAN
        details_correct = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}"
                                                        f"\nPassword: {password}")
        # if details are correct - save details to file, else do nothing
        if details_correct:
            # catch if file is not found/does not exist
            try:
                with open("data.json", "r") as data_file:
                    # 1. read data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # do this when try block is successful
                # 2. update data
                data.update(new_data)
            
                with open("data.json", "w") as data_file:
                    # 3. write new data
                    json.dump(data, data_file, indent=4)    # write to json file with indents -> improve readability
                
            finally:    
                # delete entry characters -> restart cursor
                website_entry.delete(0, END)    
                password_entry.delete(0, END)

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
gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(column=2, row=3)

# add Button - add, width 43
add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()