import tkinter
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
timer: str | None = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global timer
    if timer is not None:
        window.after_cancel(timer)

    timer_label.configure(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    check_mark.configure(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.configure(text="Chill", fg=RED)

    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.configure(text="Break", fg=PINK)

    else:
        countdown(work_sec)
        timer_label.configure(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    check_mark_list = ["✓", "✓✓", "✓✓✓", "✓✓✓✓"]
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count < 10:
        count_sec = f"0{count_sec}"

    elif count_sec == 0:
        count_sec = "00"

    if count > 0:
        global timer
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, countdown, count - 1)

    else:
        start_timer()
        if reps == 2:
            check_mark.configure(text=check_mark_list[0])

        elif reps == 4:
            check_mark.configure(text=check_mark_list[1])

        elif reps == 6:
            check_mark.configure(text=check_mark_list[2])

        elif reps == 8:
            check_mark.configure(text=check_mark_list[3])


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro innit")
window.config(padx=100, pady=50, bg=YELLOW)

# tomato picture import and setup
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

# timer text display
timer_label = tkinter.Label(
    text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN
)
timer_label.grid(column=1, row=0)

# buttons
start_button = tkinter.Button(text="start", highlightthickness=0, command=start_timer)
reset_button = tkinter.Button(text="reset", highlightthickness=0, command=reset_timer)

start_button.grid(column=0, row=2)
reset_button.grid(column=3, row=2)

# checkmarks
check_mark = tkinter.Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

window.mainloop()
