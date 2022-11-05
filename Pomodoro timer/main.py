# This is the Pomodoro timer to help you study
# it's just a cronometer but it was made with
# TKinter, so it looks pretty.


import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
# los codigos de los colores salieron de la pagina "colourhunt"
FONT_NAME = "Courier"
WORK = 25
S_BREAK = 5
L_BREAK = 20
reps = 0
routine = [WORK, S_BREAK, WORK, S_BREAK, WORK, S_BREAK, WORK, L_BREAK]
routine_text = ["Work time", "Short break", "Work time", "Short break", "Work time", "Short break", "Work time", "Long break"]
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    label.config(text = "Timer")
    canvas.itemconfig(timer_text, text = "00:00")
    check_symbol.config(text = "")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    count_down(routine[reps]*60)
    label.config(text= f"{routine_text[reps]}", fg=RED)
    reps += 1
    if reps >8:
        pass
    marks = ""
    for _ in range(math.floor(reps/2)):
        marks += "✓"
        check_symbol.config(text = marks)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_seg = count % 60
    if count_seg < 10:
        count_seg = f"0{count_seg}"
    if count_seg == 0:
        count_seg = "00"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_seg}")
    if count >0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width= 200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 22, "bold"))
canvas.grid(column=1, row=1) 

label = tkinter.Label(text = "Timer", fg = GREEN, bg=YELLOW, font=(FONT_NAME, 34, "bold"))
label.grid(column=1, row=0)

Start = tkinter.Button(text= "Start", command=start_timer)
Start.grid(column=0, row=2)

Reset = tkinter.Button(text= "Reset", command=reset_timer)
Reset.grid(column=2, row=2)

check_symbol = tkinter.Label(fg = GREEN, bg=YELLOW, font=(FONT_NAME, 22, "bold"))
check_symbol.grid(column=1, row=3)









window.mainloop()