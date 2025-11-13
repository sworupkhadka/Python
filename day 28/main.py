from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"           # Short break color
RED = "#e7305b"            # Long break color
GREEN = "#9bdeac"          # Work session color
YELLOW = "#f7f5dd"         # Background color
FONT_NAME = "Courier"      
WORK_MIN = 1               # Work session duration (minutes)
SHORT_BREAK_MIN = 5        # Short break duration (minutes)
LONG_BREAK_MIN = 20        # Long break duration (minutes)
reps = 0                   # Count of sessions
timer = None               # Reference to the after() timer

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)           # Stop current timer
    reps = 0                             # Reset session count
    canvas.itemconfig(timer_text, text="00:00")  # Reset timer display
    title_label.config(text="Timer", fg=GREEN)  # Reset label
    check_mark.config(text="")                   # Clear checkmarks

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1                             # Increment session count

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Decide which session to run
    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)   # Minutes
    count_sec = count % 60               # Seconds
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")  # Display

    if count > 0:
        timer = window.after(1000, count_down, count - 1)  # Call every second
    else:
        start_timer()                                     # Start next session automatically
        marks = "✓" * math.floor(reps / 2)                # Add checkmarks for work sessions
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

# Title label

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(row=0, column=1)

# Tomato image and timer text

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Buttons

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Checkmarks for completed work sessions

check_mark = Label(bg=YELLOW, fg=GREEN)
check_mark.grid(row=3, column=1)

window.mainloop()                                  # Run the GUI
