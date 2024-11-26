import tkinter as tk

def start_timer():
    global start_time
    start_time = time.time()
    timer_label.config(text="Timer started")

def stop_timer():
    global start_time
    end_time = time.time()
    elapsed_time = end_time - start_time
    timer_label.config(text=f"Elapsed time: {elapsed_time:.2f} seconds")

# Create the main window
window = tk.Tk()
window.title("NoHassle Time Tracker")

# Create the timer label
timer_label = tk.Label(window, text="Timer stopped")
timer_label.pack()

# Create the start and stop buttons
start_button = tk.Button(window, text="Start", command=start_timer)
start_button.pack()
stop_button = tk.Button(window, text="Stop", command=stop_timer)
stop_button.pack()

window.mainloop()
#