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
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1

    work_sec = WORK_MIN*60
    short_brk_sec = SHORT_BREAK_MIN*60
    long_brk_sec= LONG_BREAK_MIN*60

    if reps%8==0:
        start_countdown(long_brk_sec)
        timer_label.config(fg=RED,text="Long Break")
    elif reps%2 == 0:
        start_countdown(short_brk_sec)
        timer_label.config(fg=PINK, text="Short Break")
    else:
        start_countdown(work_sec)
        timer_label.config(fg=GREEN, text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_countdown(count):
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=canvas.after(1000, start_countdown, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✓"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodora")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text= canvas.create_text(102,130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(row=1, column = 1)

timer_label = Label(text="TIMER",fg=GREEN,bg=YELLOW, font=("arial",24,"normal"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row = 2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row = 2, column=2)

check_marks = Label(text="",fg=GREEN,bg=YELLOW, font=("arial",28,"bold"))
check_marks.grid(row=3,column=1)



window.mainloop()