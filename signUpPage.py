from tkinter import *
from tkinter import messagebox
import ast

"""
Program: FinalProject.py/signUpPage.py
Author: Josh Swilling
Goal: Create a Login GUI that can be easily integrated, taking in several types of input.
1. Significant constants
    PASSWORD
    USERNAME
2. The inputs are
    Password and Username
3. Computations:
    comparison of text strings (User) and Integers (Password)
4. The outputs are
 Login success/Failure/Help/Register an account
"""
from tkinter import messagebox
import ast

window = Tk()
window.title("SignUp")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)

img = PhotoImage(file='signup.png')
Label(window, image=img, border=0, bg='white').place(x=50, y=50)

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


window.mainloop()
