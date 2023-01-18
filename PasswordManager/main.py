from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_letters + password_numbers
    shuffle(password_list)

    password_list = "".join(password_list)

    password_entry.insert(0, password_list)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Oops", message=f"Please don't leave any fields empty!")
    else:
        if messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email},\n password: {password},\n Is it okay to save?"):
            with open("datafile.txt", "a") as data:
                data.write(f"\n{website} | {email} | {password}")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
#Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Picture setup
MYPASS = PhotoImage(file="logo.png")
my_canvas = Canvas(width=200, height=200)
my_canvas.create_image(100, 100, image=MYPASS)
my_canvas.grid(column=1, row=0)

#Label setup
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entry setups
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_username_entry = Entry(width=50)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "Diamondporing@hotmail.com")

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

#Button setup
generate_password_button = Button(text="Generate Password", width=25, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=48, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
