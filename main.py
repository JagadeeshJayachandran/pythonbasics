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
def reset_timer():
    """Timer reset"""
    window.after_cancel(timer)
    #   timer_text 00:00
    canvas.itemconfig(timer_text, text=f"00:00")
    #   title label "Timer"
    timer_label.config(text="Timer", fg=GREEN)
    #    reset check_marks
    green_tick.config(text="")
    global reps
    reps = 0


# title_label


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # If it's the 1st/3rd/5th/7th rep:
    print(reps % 2)
    reps += 1
    if (reps % 2 != 0):
        count_down(work_sec)
        timer_label.config(text="Work", fg=RED)
    #     If it's the 8th rep:
    elif (reps % 8 == 0):
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=PINK)
    #     If it's 2nd/4th/6th rep:
    elif (reps % 2 == 0):
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        green_tick.config(text=marks)
        # if reps % 2 == 0:
        #


# count = 5
# while True:
#     time.sleep(1)
#     count -= 1
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=("Arial", 20, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)
timer_label.config(padx=20, pady=5)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.create_text()
canvas.grid(column=1, row=1)
# canvas.config(padx=20, pady=5)

button_start = Button(text="Start", command=start_timer, font=("Arial", 12, "bold"))
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_timer, font=("Arial", 12, "bold"))
button_reset.grid(column=2, row=2)

green_tick = Label(font=("Arial", 20, "bold"), fg=GREEN, bg=YELLOW)
green_tick.grid(column=1, row=3)
green_tick.config(padx=20, pady=5)

window.mainloop()
