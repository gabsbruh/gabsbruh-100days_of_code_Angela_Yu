import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #

FONT = ("Courier", 10, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    """ Attachable to a button. Generate new password for user consist of random letters, numbers
    and special characters. 8 - 32 chars.
    """
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pwd():
    """Function attachable to the button. Designed for saving password to a file with all pasword which program is holding
    """
    pass
# ---------------------------- UI SETUP ------------------------------- #

# main window
window = tk.Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

# canvas widget to hold the logo
canvas = tk.Canvas(width=200, height=200)
logo = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo) # first two vairables stnads for place for the image
canvas.grid(column=1, row=0)

######### LABELS #########
website = tk.Label(text='Website: ', font=FONT)
website.grid(column=0, row=1)

username = tk.Label(text="Email/Username: ", font=FONT)
username.grid(column=0, row=2)

password = tk.Label(text='Password: ', font=FONT)
password.grid(column=0, row=3)

######### INPUTS #########

website_entry = tk.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

column_entry = tk.Entry(width=35)
column_entry.grid(column=1, row=2, columnspan=2)

password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3)

######### BUTTONS #########

generate = tk.Button(text="Generate Password", command=generate_pwd)
generate.grid(column=2, row=3)

add = tk.Button(text='Add', command=add_pwd, width=36)
add.grid(column=1, row=4, columnspan=2)

# main loop of program
window.mainloop()