from tkinter import *
import math

#---------------- CONSTANTS ------------------------

PINK = "#e2979c"
RED = "#e7305b"
DARK_GREEN = "#2b7a0b"
YELLOW = "#f7f5dd"

FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 1
timer = ""

# -------------- TIMER MECHANISM ---------------------


def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=PINK)
        reps_label.config(text=f"REPS: {reps // 2}")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
        reps_label.config(text=f"REPS: {reps // 2}")
    else:
        count_down(work_sec)
        timer_label.config(text="Work!", fg=DARK_GREEN)

# -------------- COUNTDOWN MECHANISM -----------------


def reset_reps():
    global reps
    reps = 1
    window.after_cancel(timer)
    reps_label.config(text="REPS: 0")
    timer_label.config(text="TIMER", fg=DARK_GREEN)
    canvas.itemconfig(timer_text, text="00:00")


def increase_reps():
    global reps
    reps += 1


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)

# -------------- UI SETUP ----------------------------


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#------------- BACKGROUND ----------------------------
canvas = Canvas(width=300, height=224, bg=YELLOW)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(150, 112, image=tomato)

timer_text = canvas.create_text(152, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")

canvas.config(highlightthickness=0)
canvas.grid(row=2, column=2)


# ------------ BUTTONS ------------------------------
start_button = Button(text="Start", fg=DARK_GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(row=3, column=1)

check_button = Button(text="✔", fg=DARK_GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"), command=increase_reps)
check_button.grid(row=4, column=2)

reset_button = Button(text="reset", fg=DARK_GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"), command=reset_reps)
reset_button.grid(row=3, column=3)

# ------------ LABELS -------------------------------
timer_label = Label(text="TIMER", fg=DARK_GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=1, column=2)

reps_label = Label(text=f"REPS: 0", fg=DARK_GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
reps_label.grid(row=0, column=2)


window.mainloop()


