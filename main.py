from tkinter import *
import time
import threading


window = Tk()
window.title("TYPING")
window.minsize(width=500, height=500)

def callback(sv):
    print(sv.get())
    global count_down
    count_down = 5


count_down = 5
game_is_on = True
def uhr():
    global game_is_on
    global count_down
    while game_is_on == True:
        time.sleep(1)
        count_down -= 1
        if count_down == 0:
            # game_is_on = False
            user_input.delete(0, END)
        print(count_down)
thread1 = threading.Thread(target=uhr)
sv = StringVar()

sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))

user_input = Entry(window, textvariable=sv, font = "Helvetica 20 bold")
user_input.pack(expand=True, fill='both')

thread1.start()

window.mainloop()