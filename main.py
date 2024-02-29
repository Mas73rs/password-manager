from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
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