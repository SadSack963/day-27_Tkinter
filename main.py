import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=300, height=200)

# Label
my_label = tkinter.Label(text="My label", font=("Arial", 16, "bold"))  # Create the label
my_label.pack()  # Specify layout on the screen (default: top center)
"""
In contrast to the more cumbersome placer,the packer takes 
qualitative relationship specification - above, to the left of, 
filling, etc - and works everything out to determine the exact 
placement coordinates for you. The size of any master widget 
is determined by the size of the “slave widgets” inside it.
https://docs.python.org/3.9/library/tkinter.html#the-packer
"""

# Modify an attribute
my_label["text"] = "New text"
my_label.config(text="New text")


# Button
def button_onclick():
    new_text = e1.get()
    my_label.config(text=new_text)


my_button = tkinter.Button(text="Click Me!", command=button_onclick)
my_button.pack()

# Entry
e1 = tkinter.Entry(width=15)
e1.pack()
# print(e1.get())  # Prints nothing because the code runs immediately after object creation


# Just like Turtle Graphics, this must be the last line of the program
window.mainloop()  # Keep the window open
