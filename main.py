import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=300, height=200)

# Label
my_label = tkinter.Label(text="My label", font=("Arial", 16, "bold"))  # Create the label
my_label.pack()  # Specify layout on the screen (default: top center)
"""In contrast to the more cumbersome placer,the packer takes 
qualitative relationship specification - above, to the left of, 
filling, etc - and works everything out to determine the exact 
placement coordinates for you."""


# Just like Turtle Graphics, this must be the last line of the program
window.mainloop()  # Keep the window open
