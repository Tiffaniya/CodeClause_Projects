# Import necessary libraries
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import random
import string
import pyperclip

# Define colors for the GUI
bg_color = '#99d6ff'  # Background color
fg_color = '#002e4d'  # Foreground color
white = '#ffffff'  # White color


# Function to generate passwords based on user input
def generator():
    password_length = int(pwd_length_box.get())
    pwd_field.delete(0, END)
    if password_length >= 17 or password_length <= 4:
        messagebox.showinfo('Error', 'Invalid Number')
    if type_box.get() == "Letters":
        pwd_field.insert(0, ''.join(random.sample(string.ascii_letters, password_length)))
    elif type_box.get() == "Numbers":
        pwd_field.insert(0, ''.join(random.sample(string.digits, password_length)))
    elif type_box.get() == "Both":
        all_chars = string.ascii_letters + string.digits
        pwd_field.insert(0, ''.join(random.sample(all_chars, password_length)))
    messagebox.showinfo('Success', 'Password Generated')




# Function to copy generated password to clipboard
def copy():
    pwd_copy = pwd_field.get()
    pyperclip.copy(pwd_copy)


# Initialize the Tkinter window
root = Tk()
root.title('Password Generator')  # Title of the GUI
root.geometry('350x250')  # Set initial size of the window
root.resizable(width=FALSE, height=FALSE)  # Prevent window resizing
root.configure(bg=bg_color)  # Set the background color

# Create a frame for organizing GUI elements
frame = Frame(root, width=300, height=400, bg=bg_color, highlightbackground="#394B6C", highlightthickness=4)
frame.pack(side=TOP, fill=X)

# Labels and input fields for password length and type selection
pwd_label = Label(frame, text="Password Generator", font=("COPPERPLATE GOTHIC BOLD", 16),
                  bg=bg_color, fg='#1A2A56')
pwd_label.place(x=43, y=15)

pwd_length = Label(frame, text='Length:', font=("Helvetica", 11, "bold"), bg=bg_color, fg=fg_color)
pwd_length.place(x=50, y=70)

pwd_length_box = Combobox(frame, font="Calibri 10 bold", width=3)
pwd_length_box['values'] = ("5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16")
pwd_length_box.current(0)
pwd_length_box.place(x=115, y=72)

pwd_type = Label(frame, text='Type:', font=("Helvetica", 11, "bold"), bg=bg_color, fg=fg_color)
pwd_type.place(x=170, y=70)

type_box = Combobox(frame, font="Calibri 11", width=7, state="readonly")
type_box['values'] = ("Letters", "Numbers", "Both")
type_box.current(0)
type_box.place(x=220, y=70)

# Button to generate passwords
generate_btn = Button(frame, text='Generate Password', font=("Tahoma", 9, 'bold'),
                      bg=fg_color, fg=white, command=generator)
generate_btn.place(x=110, y=115)

# Display field for generated passwords
pwd_field = Entry(frame, font=("Calibri", 12), width=25, bd=2)
pwd_field.place(x=68, y=160)

# Button to copy generated password to clipboard
copy_btn = Button(frame, text='Copy', font=("Tahoma", 9, 'bold'), bg=fg_color, fg=white, command=copy, width=6)
copy_btn.place(x=140, y=200)

# Start the main GUI loop
root.mainloop()
