from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any"
                                                  "fields empty")
    else:
        try:
            with open('./data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open('./data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open('./data.json', 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            # Delete entries from the app's entry fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# --------------------- FIND PASSWORDS ------------------------ #
def find_password():
    """
    Retrieves and displays the email and password information for a specified website.

    The function retrieves the website name entered by the user. It then searches a JSON data file
    for the corresponding email and password, ignoring case sensitivity. If the website is found,
    it displays the email and password. Otherwise, it informs the user that no details exist for the
    specified website. If the data file is missing, an error message is shown.

    Raises:
        FileNotFoundError: If the data file does not exist.
    """

    searched_website = website_entry.get().lower()

    try:
        with open('./data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found.')
    else:
        saved_websites = [website.lower() for website in data.keys()]

        if searched_website in saved_websites:
            # Retrieve the location of the website in the data's dictionary
            website_index = saved_websites.index(searched_website)
            # Retrieve the correct key to search for
            website_key = list(data.keys())[website_index]
            # Search the data using the correct key
            website_info = data[website_key]
            # Print the obtained info
            messagebox.showinfo(title=searched_website,
                message=f'Email: {website_info['email']}\n'
                        f'Password: {website_info['password']}')
        else:
            messagebox.showinfo(title=searched_website, message='No details for the website exists.')


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

# ROW 1: Website
website_label = Label(text='Website:', justify='center')
website_label.grid(row=1, column=0)
website_entry = Entry(width=22)
website_entry.grid(row=1, column=1)
website_entry.focus()
search_button = Button(text='Search', width=11, command=find_password)
search_button.grid(row=1, column=2)

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
generate_button = Button(text='Generate Password', width=11, command=generate_password)
generate_button.grid(row=3, column=2)

# ROW 4: Add
add_button = Button(text='Add', command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()
