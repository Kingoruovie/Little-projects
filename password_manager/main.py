from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list_letters = [random.choice(letters) for char_l in range(nr_letters)]
    password_list_symbols = [random.choice(symbols) for char_s in range(nr_symbols)]
    password_list_numbers = [random.choice(numbers) for char_n in range(nr_numbers)]
    password_list = password_list_letters + password_list_symbols + password_list_numbers
    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"username: {data[website]['username']}"
                                                   f"\npassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message="This website does not exit in this file")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_email_entry.get()
    password = password_entry.get()
    pyperclip.copy(password)
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please fill in the password or website entry")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nUsername: {username}"
                                                              f"\nPassword: {password}\nIs This Ok?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Working with json
                    # Reading a json file
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Writing to a json file
                    json.dump(new_data, data_file, indent=4)
            else:
                # Adding to a json file
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Writing to a json file
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("MY PASSWORD MANAGER")

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Arial", 10, "normal"))
website_label.grid(row=1, column=0)
website_entry = Entry(width=31)
website_entry.focus()
website_entry.grid(row=1, column=1)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

username_email_label = Label(text="Username/Email:", font=("Arial", 10, "normal"))
username_email_label.grid(row=2, column=0)
username_email_entry = Entry(width=50)
username_email_entry.insert(0, "oruovie@gmail.com")
username_email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", font=("Arial", 10, "normal"))
password_label.grid(row=3, column=0)
password_entry = Entry(width=31)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
