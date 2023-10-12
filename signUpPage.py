from tkinter import *
from tkinter import messagebox
import ast
import subprocess

"""
Program: FinalProject.py/signUpPage.py
Author: Josh Swilling
Goal: Create a Registration GUI that can be easily integrated, taking in several types of input.
1. Significant constants
    PASSWORD
    USERNAME
2. The inputs are
    Password and Username, and confirmation
3. Computations:
    comparison of text strings (User) and Integers (Password)
4. The outputs are
 Failure/Registered accounts
"""
from tkinter import messagebox
import ast

# Create the main registration window
window = Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)


# Function for handling user sign-up
def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    file = open('datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username == 'Username':
        messagebox.showinfo('Error:', 'Please enter a valid username.')
    elif username in r.keys():
        messagebox.showinfo('Error:', 'Taken, Please enter a valid username.')
    elif password == confirm_password:
        try:
            # Read existing user data from a file
            file = open('datasheet.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            # Update user data with the new username and password
            dict2 = {username: password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            # Write the updated data back to the file and display a success message
            file = open('datasheet.txt', 'w')
            w = file.write(str(r))

            messagebox.showinfo('Register', 'Successfully Registered!')
        except:
            # Create a new file with default data if there's an issue
            file = open('datasheet.txt', 'w')
            pp = str({'Username': 'password'})
            file.write(pp)
            file.close()

    else:
        # Display an error message if passwords do not match
        messagebox.showinfo('Error:', 'Passwords do not match.')


def log():
    window.destroy()
    subprocess.Popen(['python', 'SwillingJoshuaFinalProject.py'])


# Load an image for the registration form
img = PhotoImage(file='signup.png')
Label(window, image=img, border=0, bg='white').place(x=50, y=50)

# Create a frame for labels and input fields
frame = Frame(window, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

heading = Label(frame, text='Register an Account', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23,
                                                                                   'bold'))
heading.place(x=13, y=5)

"""----------------------------------Username---------------------------------------- """


# create functions for a responsive placeholder text
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Username')


# creates field for username
user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=115)
user.insert(0, 'Username')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=142)

"""----------------------------------Password---------------------------------------- """


# create functions for a responsive placeholder text
def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    if code.get() == '':
        code.insert(0, 'Password')


code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=200)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=227)

"""----------------------------------Confirm Password---------------------------------------- """


# create functions for a responsive placeholder text
def on_enter(e):
    confirm_code.delete(0, 'end')


def on_leave(e):
    if confirm_code.get() == '':
        confirm_code.insert(0, 'Confirm Password')


confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
confirm_code.place(x=30, y=280)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind("<FocusIn>", on_enter)
confirm_code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=307)

"""----------------------------------Button---------------------------------------- """
Button(frame, width=39, pady=7, text='Sign Up!', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=357)
label = Label(frame, text='Already have an account ? --', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
label.place(x=35, y=320)

# Link to the Sign-In Page
signin = Button(frame, width=6, text='Log In', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=log)
signin.place(x=190, y=320)


# Start the Tkinter event loop to run the registration GUI
window.mainloop()
