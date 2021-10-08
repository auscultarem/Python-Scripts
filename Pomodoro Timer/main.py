from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
SECONDS = 10
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
	global rep
	window.after_cancel(timer)
	rep = 0
	canvas.itemconfig(timer_text, text ="00:00")
	title = Label(text="     Timer    ", bg=YELLOW)
	title.config(fg=GREEN, font=(FONT_NAME, 30))
	title.grid(column=1, row=0)

# ----------------------------CONFIG TIMER ---------------------------------- #
def config_timer():
	global rep

	if rep == 1 or rep == 3 or rep == 5:
		title = Label(text="  WORK TIME   ", bg=YELLOW)
		title.config(fg=PINK, font=(FONT_NAME, 30))
		title.grid(column=1, row=0)

	elif rep == 2 or rep == 4:
		title = Label(text="  BREAK TIME  ", bg=YELLOW)
		title.config(fg=RED, font=(FONT_NAME, 30))
		title.grid(column=1, row=0)

	else:
		title = Label(text="LONG BREAK TIME", bg=YELLOW)
		title.config(fg=RED, font=(FONT_NAME, 30))
		title.grid(column=1, row=0)


# ---------------------------- PRINT LABEL ---------------------------------- #
def print_label():
	global rep
	check_mark = Label(text="✔️" * rep, fg=GREEN, bg=YELLOW)
	check_mark.grid(column=1, row=3)
	
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def star_timer():
	global rep
	rep += 1

	work_sec = WORK_MIN * SECONDS
	short_break_sec = SHORT_BREAK_MIN * SECONDS
	long_break_sec = LONG_BREAK_MIN * SECONDS

	if rep == 1 or rep == 3 or rep == 5:
		count_down(work_sec)
		config_timer()
		print_label()

	elif rep == 2 or rep == 4:
		count_down(short_break_sec)
		config_timer()
		print_label()
	else:
		count_down(long_break_sec)
		config_timer()
		print_label()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
	
	count_min = math.floor(count / 60)
	count_sec =  count % 60
	if count_sec < 10:
		count_sec = f"0{count_sec}"	
	
	
	canvas.itemconfig(timer_text, text =f"{count_min}:{count_sec}")
	if count > 0:
		global timer
		timer = window.after(1000,count_down, count -1)
	
	


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)



canvas = Canvas(width = 200, height = 224,
								 bg = YELLOW, highlightthickness = 0)

tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= tomato_image)

timer_text = canvas.create_text(100, 130, text ="00:00", fill = "white",
                   font= (FONT_NAME, 20, "bold"),
									  )
canvas.grid(column = 1, row = 1)

title = Label(text="Timer", bg= YELLOW)
title.config(fg= GREEN, font = (FONT_NAME, 30))
title.grid(column = 1, row = 0)

start = Button(text="Start", bg = "white", highlightthickness = 0, command = star_timer)
start.grid(column = 0, row = 2)


reset = Button(text = "Reset", bg = "white", highlightthickness = 0, command = reset_timer)
reset.grid(column = 2, row = 2)

window.mainloop()