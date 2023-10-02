from tkinter import *

"""
Program: FinalProject.py
Author: Josh Swilling
Goal: Create a Login GUI
1. Significant constants

2. The inputs are
    Password and Username
3. Computations:

4. The outputs are
 Login success/Failure/Help/Register an account
"""

""" create project and the dimensions for the login form and generate the window """

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

""" define and configure loading screen on successful login"""


def signin():
    username = user.get()
    password = code.get()

    if username == 'admin' and password == '1234':
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen, text='Hello!', bg='#fff', font=('Calibre(Body)', 50, 'bold')).pack(expand=True)

        screen.mainloop()


""" add Image 1 and translate it """
img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

""" Frame div area for labels and text input """
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

""" Label 1 placement and text """
heading = Label(frame, text='Welcome, Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=35, y=5)


""" Format a seamless input with no borders and placeholder text prompt that deletes on entering text field """


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
# bind
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
# ---------------------------------------------------------


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=175)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=203)

""" Format submit buttons for input submission """
Button(frame, width=19, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, cursor='hand2', command=signin).place(x=23, y=254)

Button(frame, width=19, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, cursor='hand2').place(x=185, y=254)

""" create help link for sign in issues """
help_img = PhotoImage(file='dot.png')
Label(root, image=help_img, bg='white').place(x=520, y=379)

help_link = Button(frame, width=20, pady=7, text='Need help signing in?', bg='white', fg='#57a1f8', border=0,
    cursor='hand2')
help_link.place(x=85, y=320)

root.mainloop()