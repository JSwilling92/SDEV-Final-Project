from tkinter import *

"""
Program: FinalProject.py/userManual.py
Author: Josh Swilling
Goal: Create a user manual, explaining how to manage the application.
1. Significant constants
    PASSWORD
    USERNAME
2. The inputs are
    Password and Username
3. Computations:
    comparison of text strings (User) and Integers (Password)
4. The outputs are
    the user manual(string)
"""


# Define a function to configure the canvas scroll region
def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


# Define a function to handle mouse wheel events for scrolling
def on_mouse_wheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")


# Create a Tkinter window for the user manual
user_manual = Tk()
user_manual.title("User Manual")
user_manual.geometry('800x600')  # Removed positioning for centering
user_manual.configure(bg='#f0f0f0')  # Updated background color

# Center the window on the screen
window_width = user_manual.winfo_reqwidth()
window_height = user_manual.winfo_reqheight()
screen_width = user_manual.winfo_screenwidth()
screen_height = user_manual.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
user_manual.geometry('+{}+{}'.format(x, y))

# Create a canvas with a scrollbar for vertical scrolling
canvas = Canvas(user_manual, bg='#f0f0f0')  # Updated canvas background color
canvas.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(user_manual, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", on_canvas_configure)

# Bind mouse wheel events to the canvas
user_manual.bind("<MouseWheel>", on_mouse_wheel)

# Create a frame for the content
content_frame = Frame(canvas, bg='#f0f0f0')  # Updated frame background color
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Title
title = Label(content_frame, text='User Registration User Manual', fg='#57a1f8', bg='#f0f0f0',
              font=('Arial', 24, 'bold'))  # Updated font and colors
title.pack(pady=20)  # Increased padding

# Add an image
img = PhotoImage(file='signup.png')
img_label = Label(content_frame, image=img, bg='#f0f0f0')
img_label.pack(pady=20)

# Introduction
intro_label = Label(content_frame, text="Welcome to our user registration system!", fg='black', bg='#f0f0f0',
                    font=('Arial', 16))
intro_label.pack(pady=20, padx=20, anchor='w')

# Instructions
instructions_label = Label(content_frame, text="Follow these steps to create your account:", fg='black', bg='#f0f0f0',
                            font=('Arial', 16))
instructions_label.pack(pady=20, padx=20, anchor='w')

# Step 1: Registering an Account
step1_label = Label(content_frame, text="Step 1: Registering an Account", fg='#57a1f8', bg='#f0f0f0',
                    font=('Arial', 14, 'bold'))
step1_label.pack(pady=10, padx=20, anchor='w')
step1_text = Label(content_frame, text="1. Start the application by double-clicking the application icon.", fg='black',
                   bg='#f0f0f0', font=('Arial', 14))
step1_text.pack(pady=10, padx=20, anchor='w')
# ... (other registration steps)

# Step 2: Logging In
step2_label = Label(content_frame, text="Step 2: Logging In", fg='#57a1f8', bg='#f0f0f0',
                    font=('Arial', 14, 'bold'))
step2_label.pack(pady=10, padx=20, anchor='w')
step2_text = Label(content_frame, text="1. Open the application by double-clicking the application icon.", fg='black',
                   bg='#f0f0f0', font=('Arial', 14))
step2_text.pack(pady=10, padx=20, anchor='w')
step2_text = Label(content_frame, text="2. Click the 'Log In' button to access the login page.", fg='black',
                   bg='#f0f0f0', font=('Arial', 14))
step2_text.pack(pady=10, padx=20, anchor='w')
step2_text = Label(content_frame, text="3. Enter your username and password in the respective fields.", fg='black',
                   bg='#f0f0f0', font=('Arial', 14))
step2_text.pack(pady=10, padx=20, anchor='w')
step2_text = Label(content_frame, text="4. Click the 'Log In' button to access your account.", fg='black',
                   bg='#f0f0f0', font=('Arial', 14))
step2_text.pack(pady=10, padx=20, anchor='w')
# ... (other login steps)

# Additional Information
info_label = Label(content_frame, text="For additional help, refer to the user manual or contact support.", fg='black',
                   bg='#f0f0f0', font=('Arial', 14))
info_label.pack(pady=20, padx=20, anchor='w')

# Update the canvas configuration
user_manual.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Main loop
user_manual.mainloop()
