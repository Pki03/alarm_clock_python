from tkinter import *
import datetime
import time
import winsound
from threading import Thread

def threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
        
        if current_time == set_alarm_time:
            print("It's time to wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            
        time.sleep(1)  # Sleep for 1 second

root = Tk()
root.geometry("400x200")

Label(root, text="Alarm Clock", fg="red").pack(pady=10)
Label(root, text="Set Time").pack()

frame = Frame(root)
frame.pack()

hours = [str(i).zfill(2) for i in range(24)]
hour = StringVar(root)
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minutes = [str(i).zfill(2) for i in range(60)]
minute = StringVar(root)
minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

seconds = [str(i).zfill(2) for i in range(60)]
second = StringVar(root)
second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(root, text="Set Alarm", command=threading).pack(pady=20)

root.mainloop()
