import tkinter as tk
from datetime import datetime

def update_name():
    name = name_entry.get()
    current_time = datetime.now().strftime("%H:%M:%S")
    name_label.config(text="Your Name: " + name + " (Current Time: " + current_time + ")")

# Create Tkinter window
root = tk.Tk()
root.title("Update Name")

# Create entry field for entering name
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=0, padx=5, pady=5)

# Create button to update name
update_button = tk.Button(root, text="Update", command=update_name)
update_button.grid(row=0, column=1, padx=5, pady=5)

# Create label to display name and current time
name_label = tk.Label(root, text="Your Name: ")
name_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()

