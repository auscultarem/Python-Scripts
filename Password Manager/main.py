from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- CONSTANT------------------------------- #
WHITE = "#FDFEFF"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    #password_list = []
    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for letter in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for letter in range(nr_numbers)]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)

    #print(f"Your password is: {password}")
    password_entry.insert(0, string=password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_content = website_entry.get()
    email_content = email_entry.get()
    password_content = password_entry.get()

    if website_content == "" or password_content == "":
        messagebox.showwarning(title=website_content, message="There are empty entries")
    else:
        pass

    is_ok = messagebox.askokcancel(title=website_content, message="Is it ok?")

    if is_ok:
        content = f"{website_content} | {email_content} | {password_content} \n"
        with open("Password_Manager.txt", "a") as manager:
            manager.write(content)
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg=WHITE)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg=WHITE)
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg=WHITE)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "auscultarem@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, sticky="W")

# Buttons
generate_password = Button(text="Generate Password", bg=WHITE, command=password_generator)
generate_password.grid(column=2, row=3)
add_button = Button(text="Add", bg=WHITE, width=30, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
