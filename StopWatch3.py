import tkinter as Tkinter
from datetime import datetime, timedelta

# Initialize the counter and running variables
counter = 0
running = False


# Define the counter_label() function that updates the stopwatch display
def counter_label(label):
    # Define the nested count() function that updates the label every second
    def count():
        # Check if the stopwatch is currently running
        if running:
            # Access the global counter variable
            global counter

            # Convert the counter value to a timedelta object and format it as HH:MM:SS
            tt = timedelta(seconds=counter)
            string = str(tt)

            # Update the label text with the current time display
            label.config(text=string)

            # Schedule the next update in 1000ms (1 second)
            label.after(1000, count)
            counter += 1

    # Call the count() function to start updating the label
    count()


# Define the Start() function that starts the stopwatch
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'


# Define the Stop() function that stops the stopwatch
def Stop():
    global running
    running = False
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'


# Define the Reset() function that resets the stopwatch
def Reset(label):
    global counter, running
    counter = 0  # Reset the counter to 0
    running = False  # Stop the stopwatch if it's running
    label.config(text='Welcome!')  # Update the label text
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'disabled'


# Create the main window using Tkinter
root = Tkinter.Tk()
root.title("Stopwatch")

# Set the size of the window
root.minsize(width=250, height=70)

# Create a label to display the stopwatch time
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()

# Create a frame to hold the buttons
f = Tkinter.Frame(root)

# Create the "Start", "Stop", and "Reset" buttons
start = Tkinter.Button(f, text='Start', width=6, command=lambda: Start(label))
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))
f.pack(anchor='center', pady=5)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")

root.mainloop()
