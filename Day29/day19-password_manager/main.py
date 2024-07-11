from tkinter import *
from tkinter import messagebox
import random
# import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters= [random.choice(letters) for i in range(nr_letters)]
    password_numbers= [random.choice(numbers) for i in range(nr_numbers)]
    password_symbols= [random.choice(symbols) for i in range(nr_symbols)]

    password_list = password_symbols + password_numbers + password_letters

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    # print(f"Your password is: {password}")
    pass_input.insert(0,password)
    # pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_input.get()
    username = username_input.get()
    password = pass_input.get()

    if len(website)==0 or len(username)==0 or len(password)==0:
        messagebox.showinfo(title="oops!", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}",
                                       message=f"These are the details enetered:\nEmail: {username}\nPassword: {password}\nIs is ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {username} | {password}\n")
                web_input.delete(0, END)
                pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200,width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0, column=1)

#labels
website_label= Label(text="Website: ")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username: ")
username_label.grid(row=2, column=0)
pass_label = Label(text="Password: ")
pass_label.grid(row=3, column=0)

#entris
web_input = Entry(width=42)
web_input.grid(row=1, column=1, columnspan=2)
web_input.focus()
username_input = Entry(width=42)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "abdc@gail.com")
pass_input = Entry(width=24)
pass_input.grid(row=3, column=1)

#buttons
generate_button = Button(text="Generate Password", width=14, command=pass_gen)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()