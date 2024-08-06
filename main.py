from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char2 in range(nr_symbols)]
    password_list += [random.choice(numbers) for char3 in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password_name = password_entry.get()
    new_data = {
        website_name.capitalize(): {
            "email": email_name,
            "password": password_name,
        }
    }
    if website_name == "" or email_name == "" or password_name == "":
        messagebox.showinfo(message="You have not entered all data!", title="Oooops!")
    else:
        isok = messagebox.askokcancel(message=f"These are data you entered:\n "
                                              f"Email/Username: {email_name}\n Password: {password_name}\n"
                                              "Is it OK to save?", title=website_name)

        if isok:
            # dataset = website_name + "  |" + email_name + "  |" + password_name + "\n"
            try:
                with open("data.json", "r") as data_file:
                    # f.write(dataset)
                    #data.write(f"{website_name} | {email_name} | {password_name} \n")
                    #load
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # write
                    json.dump(new_data, data_file, indent=4)
            else:
                # update
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    # write
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website_name = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found", title="Result")
    #for website in data.keys():
    #    if website.upper() == website_name.upper():
    # This is another way to search in dictionary using keyword:
    # if website in data:
    try:
        current_password = data.get(website_name.capitalize()).get("password")
        messagebox.showinfo(message=f"Website {website_name.capitalize()}\n Password:{current_password}",
                            title="Result")
    except AttributeError:
        messagebox.showinfo(message="No details for the website exists", title="Result")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
logo = canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "s_zeinolabedin@yahoo.com")

password = Label(text="Password:")
password.grid(row=3, column=0)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(row=3, column=2)

add = Button(text="Add", width=43, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
