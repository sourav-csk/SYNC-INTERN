#=========Import Modules==========

from tkinter import *
import datetime
import time
from pygame import mixer
from PIL import Image,ImageTk

root = Tk()
root.title("My Alarm---->> 24hrs format")
root.config(bg="red")
root.geometry("478x340")
root.resizable(False,False)

#=========Variables========

hrs = StringVar()
mins = StringVar()

#=============Clock Image==============

clock = Image.open(rb"D:\SYNC Intern\Alarm-Clock\al_clock.png")
clock = ImageTk.PhotoImage(clock)
img = Label(root,image=clock)
img.place(x=0,y=0)

#==========function===========

def set_alarm():
    alm_time = f"{hrs.get()}:{mins.get()}:00"
    if alm_time != ": :00":
        alm_clock(alm_time)

#===========Set Alam===========

def alm_clock(alm_time):
    while True:
        time.sleep(1)
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now == alm_time:
            Label(root,text="Wake Up...!",bg="yellow",font=("georgia",20,"italic")).grid(padx=200,pady=10,row=2,column=2)
            print("Wake Up....")
            mixer.init()
            mixer.music.load("D:\SYNC Intern\Alarm-Clock\Alarm Clock Alarm.mp3")
            mixer.music.play(loops=3)
            break

#==========Lables -- Hours/Minutes=========

Label(root,text="Take a short nap..!",font=("gorgia",20,"italic"),bg="black",fg="red").place(x=220,y=60)
Label(root,text="Hours",font=("gorgia",16,"italic"),bg="black",fg="red").place(x=290,y=110)
Label(root,text="Minutes",font=("gorgia",16,"italic"),bg="black",fg="red").place(x=360,y=110)

#==========User Input===============

hrs_entry = Entry(root,textvariable=hrs,width=4,font=("gorgia",17,"italic"))
hrs_entry.place(x=300,y=170)

mins_entry = Entry(root,textvariable=mins,width=4,font=("gorgia",17,"italic"))
mins_entry.place(x=360,y=170)

#===================Button================

set_btn = Button(root,text="Set alarm",command=set_alarm,bg="black",fg="yellow",font=("gorgia",16,"italic"))
set_btn.place(x=300,y=240)

#=========root call==========
mainloop()