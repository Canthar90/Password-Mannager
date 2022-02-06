# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import string
from tkinter import messagebox
import pyperclip
import json


alphabet = string.ascii_letters
signs = "1234567890-=+|\?/>.,<!@#$%^&*()~`"
signs_list = list(signs)
alphabet_list = list(alphabet)

def password_generator():
    global signs_list, alphabet_list
    random.shuffle(signs_list)
    random.shuffle(alphabet_list)
    passw = [signs_list[n] for n in range(1, 12) ]
    passw += [alphabet_list[n] for n in range(1, 12)]
    random.shuffle(passw)
    passw = "".join(passw)
    password_entry.delete(0, END)
    password_entry.insert(END, string=passw)
    pyperclip.copy(passw)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    webside = webside_entry.get()
    email_user = email_user_entry.get()
    password = password_entry.get()
    new_data = {webside: {
        "email": email_user,
        "password": password,
    }}
    example = {"example webside": {
        "email": "example@gmail.com",
        "password": "examplepasword",
    }}
    if webside != '' and email_user != '' and password != '':

    # messagebox.showinfo(title="Error", message="Task Failed Succesfully")
        is_ok = messagebox.askokcancel(title=webside, message=f"These are the details entered: \nEmail: {email_user}\nPassword: "
                                                  f"{password}\n Is it ok to save?")
        if is_ok:
            try:
                with open(file="passess.json", mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open(file="passess.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open(file="passess.json", mode="w") as file:
                    json.dump(data, file, indent=4)
                    print(data)
            finally:
                password_entry.delete(0, END)
                webside_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Error", message="You left empty fields")
        messagebox.showinfo(title="Error", message="Did You know that mitohondria is a powerhouse of a cell?")



def find_password():
    webside = webside_entry.get()
    try:
        with open(file="passess.json", mode="r") as file:
            data = json.load(file)
            findet_data = data[webside.capitalize()]
            email = findet_data["email"]
            password = findet_data["password"]
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="There is no Database File my dear")
    except KeyError:
        messagebox.showinfo(title=f"Error for {webside}", message="There is no Webside with this name in Database")
    else:
        messagebox.showinfo(title=f"Password for {webside}", message=f"\nEmail: {email} \nPassword: {password} ")
        pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
jpg = PhotoImage(file="logo.png")
pictiure = canvas.create_image(100, 100, image=jpg)
canvas.grid(column=1, row=0)

webside_label = Label(text="Website: ")
webside_label.grid(column=0, row=1)

webside_entry = Entry(width=34)
webside_entry.focus()
webside_entry.grid(column=1, row=1, columnspan=1)

search_button = Button(text="Search", fg="black",  width=14, command=find_password)
search_button.grid(column=2, row=1)


email_user_label = Label(text="Email/Username: ")
email_user_label.grid(column=0, row=2)

email_user_entry = Entry(width=53)
email_user_entry.insert(END, string="example@example.com")
email_user_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()