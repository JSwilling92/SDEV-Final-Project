"""
Program: FinalProject.py
Author: Josh Swilling
Goal: Create a Login GUI
1. Significant constants

2. The inputs are
    Password and Username
3. Computations:

4. The outputs are
 Login success/Failure/Forgotten password/Register an account
"""
# create project and the dimensions for the login form and generate the window
from tkinter import *
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# add Image 1 and translate it
img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=50, y=50)

# Frame div area for labels and text input
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

# Label 1 placement and text
heading = Label(frame, text='Welcome, Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=35,y=5)


# Format a seamless input with no borders and placeholder text prompt
user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)
# ---------------------------------------------------------
code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=175)
code.insert(0, 'Password')

Frame(frame, width=295, height=2, bg='black').place(x=25, y=203)

# Format submit buttons for input submission
Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0)

root.mainloop()
