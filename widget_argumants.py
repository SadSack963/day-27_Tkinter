import tkinter as tk


# ---------------- tkinter widget keys -------------------

# Print the allowed widget keys

def get_keys(widget):
    print(f"widget: {widget}\n"
          f"keys  : {widget.keys()}\n")


get_keys(tk.Tk())
get_keys(tk.Button())
get_keys(tk.Canvas())
get_keys(tk.Checkbutton())
get_keys(tk.Entry())
get_keys(tk.Frame())
get_keys(tk.Label())
get_keys(tk.Listbox())
get_keys(tk.Menubutton())
get_keys(tk.Menu())
get_keys(tk.Message())
get_keys(tk.Radiobutton())
get_keys(tk.Scale())
get_keys(tk.Scrollbar())
get_keys(tk.Text())
get_keys(tk.Toplevel())
get_keys(tk.Spinbox())
get_keys(tk.PanedWindow())
get_keys(tk.LabelFrame())


# ---------------- tkinter widget key values -------------------

# To find out what arguments are accepted by a widget,
# together with the default/current values, use .config() without any options.
# This returns a dictionary of the allowed arguments which can then be printed out.
#
# The first entry (lowercase) is the option name
# The second item (camelCase) is the option name for database lookuo,
# The third entry (Titlecase) is the option class for database lookup,
# The fourth entry is the default value,
# The fifth item is the current value.
#
# I created a function to make the main program less cluttered,
# and the output more human readable.
# Note the encoding="utf-16" allows the checkmark to be written to the file:


# Print widget configuration
def print_config(widget, name):
    # Print to console
    print(name + " Config:")
    widget_config = widget.config()
    for item in widget_config:
        print(item, widget_config[item])
    print("\n")

    # # (create a config directory in the project tree)
    # # Write to text file
    widget_config = widget.config()
    filename = "./config/config_" + name + ".txt"
    with open(filename, mode="w", encoding="utf-16") as file:
        for item in widget_config:
            file.write(f"{item}, {widget_config[item]}\n")


print_config(widget=tk.Tk(), name="Window")
print_config(widget=tk.Button(), name="Button")
print_config(widget=tk.Canvas(), name="Canvas")
print_config(widget=tk.Checkbutton(), name="Checkbutton")
print_config(widget=tk.Entry(), name="Entry")
print_config(widget=tk.Frame(), name="Frame")
print_config(widget=tk.Label(), name="Label")
print_config(widget=tk.Listbox(), name="Listbox")
print_config(widget=tk.Menubutton(), name="Menubutton")
print_config(widget=tk.Menu(), name="Menu")
print_config(widget=tk.Message(), name="Message")
print_config(widget=tk.Radiobutton(), name="Radiobutton")
print_config(widget=tk.Scale(), name="Scale")
print_config(widget=tk.Scrollbar(), name="Scrollbar")
print_config(widget=tk.Text(), name="Text")
print_config(widget=tk.Toplevel(), name="Toplevel")
print_config(widget=tk.Spinbox(), name="Spinbox")
print_config(widget=tk.PanedWindow(), name="PanedWindow")
print_config(widget=tk.LabelFrame(), name="LabelFrame")
