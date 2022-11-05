import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR -------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "Email": email,
            "Password": password,
        }
    }

    if len(website) > 0 and len(email) > 0 and len(password) > 0:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
    else:
        messagebox.showwarning(title="Missing Data",
                               message="Please fill all available boxes")
# --------------------------------------------------------------------- #

def search():
    website = website_entry.get()
    email = email_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title=f"{website_entry.get()}",
                                     message=f"Email: {email}\n\nPassword:  " 
                                         f"{data[website]['Password']}")
    except FileNotFoundError:
        messagebox.showwarning("Missing Data File", "No Data File Found")
    except KeyError:
        messagebox.showwarning("Missing Website", "No website on record.")
    
# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = tkinter.Label(text="Website:")
website.grid(column=0, row=1)

email = tkinter.Label(text="Email/Username:")
email.grid(column=0, row=2)

password = tkinter.Label(text="Password:")
password.grid(column=0, row=3)

website_entry = tkinter.Entry(width=23)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = tkinter.Entry(width=41)
email_entry.insert(0, "sturlanicolasjavier@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = tkinter.Entry(width=23)
password_entry.grid(column=1, row=3)

generate_button = tkinter.Button(text="Generate password", command=generate_password)
generate_button.grid(column=2, row=3)

search_button = tkinter.Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)

add_button = tkinter.Button(text="Add", width=41, command=save)
add_button.grid(column=1, row=4, columnspan=2)

label = tkinter.Label(text="")
label.grid(column=1, row=0)


window.mainloop()
