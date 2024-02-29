from tkinter import *
from tkinter import messagebox
from random import  choice, randint, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any"
                                                  "fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
            message=f'These are the details entered: \nEmail: {email}'
                    f'\nPassword: {password} \nIs it ok to save?')

        if is_ok:
            try:
                with open('./data.txt', 'a') as file:
                    file.writelines(f'{website} | {email} | {password} \n')
            except PermissionError:
                print("Permission Denied: Unable to write to the file.")
            except IOError as e:
                print(f"IOError: {e}")
            print(f'New Password added for: {website} \n')

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Load image
lock_img = PhotoImage(file='./logo.png')

# Canvas with the lock logo
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# ROW 1: Website Info
website_label = Label(text='Website:', justify='center')
website_label.grid(row=1, column=0)
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky='EW')
website_entry.focus()

# ROW 2: Email/Username
email_label = Label(text='Email/Username:', justify='center')
email_label.grid(row=2, column=0)
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky='EW')
email_entry.insert(0, 'example@exapmple.com')

# ROW 3: Password
password_label = Label(text='Password:', justify='center')
password_label.grid(row=3, column=0)
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)
generate_button = Button(text='Generate Password', width=11)
generate_button.grid(row=3, column=2)

# ROW 4: Add
add_button = Button(text='Add', command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()