import tkinter


def button_onclick():
    new_text = my_entry.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="My label", font=("Arial", 16, "bold"))  # Create the label
my_label.pack(side="left")  # Specify layout on the screen (default: top center)
# my_label.place(x=100, y=150)  # Specify exact coordinates for the widget
# my_label.grid(row=0, column=0)  # Define a grid position in row, column format
"""
In contrast to the more cumbersome placer,the packer takes 
qualitative relationship specification - above, to the left of, 
filling, etc - and works everything out to determine the exact 
placement coordinates for you. The size of any master widget ("window" in this case) 
is determined by the size of the “slave widgets” inside it.
https://docs.python.org/3.9/library/tkinter.html#the-packer
"""

# Modify an attribute
my_label["text"] = "New text"
my_label.config(text="New text", padx=20, pady=20)


# Button
my_button = tkinter.Button(text="Click Me!", command=button_onclick).pack()
# my_button.pack()
# my_button.grid(row=1, column=1)
# my_button.config(padx=20, pady=20)

new_button = tkinter.Button(text="Click Me!", command=button_onclick).pack()
# my_button.pack()
# new_button.grid(row=0, column=2)
# new_button.config(padx=20, pady=20)


# Entry
my_entry = tkinter.Entry(width=15)
my_entry.pack()
# print(e1.get())  # Prints nothing because the code runs immediately after object creation
# my_entry.grid(row=3, column=3)
# my_entry.config(padx=20, pady=20)  # Doesn't work - no padding


# Just like Turtle Graphics, this must be the last line of the program
window.mainloop()  # Keep the window open
