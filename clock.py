from tkinter import *
from time import strftime

# Function to update the time every second
def update():
    time_string = strftime("%I:%M:%S %p")  # Get current time in 12-hour format with AM/PM
    time_label.config(text=time_string)   # Update the label text with current time
    time_label.after(1000, update)        # Call this function again after 1000 ms (1 second)

# Create the main application window
window = Tk()

# Set the title of the window
window.title("Clock")  

# Create and configure the time label
time_label = Label(window, font=("Arial", 50), fg="#2F00FF", bg="black")
time_label.pack()  # Add the label to the window

# Start updating the time
update()

# Start the Tkinter event loop
window.mainloop()
