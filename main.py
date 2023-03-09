# importing necessary modules
from tkinter import *
import datetime as dt
import time
import tkinter.messagebox
from playsound import playsound


# defining required function for the program
def alarm(setAlarmTimer):
    while True:
        time.sleep(1)
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%H : %M : %S")
        currentDate = actualTime.strftime("%d / %m / %Y")
        the_message = "Current Time: " + str(currentTime)
        print(the_message)
        if currentTime == setAlarmTimer:
            print('Alarm is ringing.....alarm is ringing.....')
            # tkinter.messagebox.showinfo("Alarm Notification", 'Wake Up...Wake Up')
            playsound(r"C:\Users\lenovo\Desktop\music.mp3")
            break


def AlarmTime():
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"
    alarm(alarmSetTime)


# GUI code
root = Tk()
root.title("Alarm Clock")
root.geometry("500x200")
root.resizable(width=False, height=False)
root.iconbitmap('icon.ico')

pic = PhotoImage(file='clock.png')
Label(root, image=pic).place(x=10, y=0)

Label(root, text="Set time in 24-hour format", font=('comic sans ms', 13, 'bold'), fg="#034F84").place(x=222, y=10)
Label(root, text="Hour        Minute        Second", font=('comic sans ms', 13), fg="#034F84").place(x=220, y=40)

hour = StringVar()
minute = StringVar()
second = StringVar()

Entry(root, textvariable=hour, bg="#BCD2E8", width=5, font=20).place(x=220, y=70)
Entry(root, textvariable=minute, bg="#BCD2E8", width=5, font=20).place(x=307, y=70)
Entry(root, textvariable=second, bg="#BCD2E8", width=5, font=20).place(x=403, y=70)

Button(root, text="Set Alarm", fg="white", bg='#034F84', width=11, command=AlarmTime,
       font=('comic sans ms', 13, 'bold')).place(x=270, y=120)

root.mainloop()