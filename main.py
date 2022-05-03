from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():

#Password Generator Project

    password_entry.delete(0, last=END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    the_website = website_entry.get()
    email = username_entry.get()
    the_password = password_entry.get()

    new_data = {
        the_website: {
            "email": email,
            "password": the_password
                    }
    }

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Error", message="One or more fields are empty.")
    else:
        try:
            with open(file="data.json",  mode="r") as file:
                # Reading old data
                data = json.load(file)          # data will be of type dict
        except FileNotFoundError:
            with open(file="data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:

            # Updating old data with new data dict
            data.update(new_data)
            with open(file="data.json", mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, last=END)
            password_entry.delete(0, last=END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_pass():
    entered_website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="File not found", message="File does not exists")
    else:
        if entered_website in data.keys():
            messagebox.showinfo(title=f"{entered_website}", message=f"Email: {data[entered_website]['email']}\n"
                                                                    f"Password: {data[entered_website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"There is no information for {entered_website} account")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website:", pady=10)
website.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, columnspan=2, row=1)

search_button = Button(text="Search", command=search_pass)
search_button.grid(column=2, row=1)

username = Label(text="Email/Username:", pady=10)
username.grid(column=0, row=2)
username_entry = Entry(width=35)
username_entry.insert(0, "18SE02CE015@ppsu.ac.in")
username_entry.grid(column=1, columnspan=2, row=2)

password = Label(text="Password:", pady=10)
password.grid(column=0, row=3)
password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_pass)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
