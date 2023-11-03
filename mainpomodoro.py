from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global timer
    global reps
    global timer_text

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Pomodoro", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg="black")
    check_mark.config(bg=YELLOW, fg=GREEN, highlightthickness=0)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_second = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps == 7:
        countdown(long_break)
        title.config(text="Long Break", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg="black")
        reps = 0

    elif reps % 2 == 0:
        countdown(work_second)
        title.config(text="Work Time", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=RED)
        reps += 1

    elif reps % 2 == 1:
        countdown(short_break)
        title.config(text="Pause", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=GREEN)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    minute = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minute}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        sessions = math.floor(reps/2)
        for _ in range(sessions):
            mark += "✓"
        check_mark.config(text=mark, bg=YELLOW, fg=GREEN, highlightthickness=0)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

title = Label(text="Pomodoro", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=GREEN)
check_mark = Label(bg=YELLOW, fg=GREEN, highlightthickness=0)

start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"),
                      bg=YELLOW, fg=RED, highlightthickness=0, command=start_timer)

reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"),
                      bg=YELLOW, fg=RED, highlightthickness=0, command=reset)

canvas.grid(column=2, row=2)
title.grid(column=2, row=1)
check_mark.grid(column=2, row=3)
start_button.grid(column=1, row=3)
reset_button.grid(column=3, row=3)

window.mainloop()
