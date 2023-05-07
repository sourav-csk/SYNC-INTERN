import datetime
from tkinter import *
from pygame import mixer

#======================== making GUI =====================

root = Tk()
root.title("CHATBOT JARVIS")
root.resizable(False, False)
root.config(bg="white")

#======================== Button Function =======================
#======================== Messages or Chats =====================


def send():
    send1 = "You => " + e.get()
    txt.insert(END,"\n" + send1)
    if e.get() == "Hello" or e.get() == "Hi" or e.get() == "Hey" or e.get() == "hi":
        txt.insert(END,"\n" + "Bot => Hey")
    elif e.get() == "How are you":
        txt.insert(END, "\n" + "Bot => Glad you asked..! I'm feeling amazing...😊😊")
    elif e.get() == "Good evening" or e.get() == "Gud eve" or e.get() == "ge":
        txt.insert(END, "\n" + "Bot => Very Good Evening..!")
    elif e.get() == "Good morning" or e.get() == "gm" or e.get() == "GM":
        txt.insert(END, "\n" + "Bot => Very Good Morning..!")
    elif e.get() == "What is your name?":
        txt.insert(END, "\n" + "Bot => My name is Chatbot.")
    elif e.get() == "Are you a robot?":
        txt.insert(END, "\n" + "Bot => Yes, I'm...")
    elif e.get() == "Are you human?":
        txt.insert(END, "\n" + "Bot => No, I'm Robot.")
    elif e.get() == "Who made You?":
        txt.insert(END, "\n" + "Bot => Boss made me...")
    elif e.get() == "What's your location?":
        txt.insert(END, "\n" + "Bot => Currently UP ")
    elif e.get() == "I hava a question..":
        txt.insert(END, "\n" + "Bot => Please ask, may be I can help you.. ")
    elif e.get() == "Do you know a joke?":
        txt.insert(END, "\n" + "Bot => Yes, Why are cricket stadiums so cool? ")
        txt.insert(END, "\n" + "       Because every seat has a fan in it.....")
    elif e.get() == "Do You want to drink water?":
        txt.insert(END, "\n" + "Bot => I've never tried water. I get my energy from answering questions.")
    elif e.get() == "Do you like to chat?":
        txt.insert(END, "\n" + "Bot => It's the highlight of my day..")
    elif e.get() == "I like talking with you":
        txt.insert(END, "\n" + "Bot => I like talking with you too! We are like salt & pepper. ")
    elif e.get() == "Tell me something about me":
        txt.insert(END, "\n" + "Bot => You're smart and you ask me great questions...")
    elif e.get() == "Do you have a nickname?":
        txt.insert(END, "\n" + "Bot => No, I'm just your friendly assistant. But you can say me Nicky..!")
    elif e.get() == "Who is your boss?":
        txt.insert(END, "\n" + "Bot => Sunaina..... ")
    elif e.get() == "What is the current time?":
        txt.insert(END, "\n" + "Bot => " + datetime.datetime.now().strftime("%H:%M:%S"))
    elif e.get() == "Which language you know?":
        txt.insert(END, "\n" + "Bot => I know python.")
    elif e.get() == "Tell me about yourself.":
        txt.insert(END, "\n" + "Bot => I am your assistant, I'm Here to help you. Let me know if you need anything...")
    elif e.get() == "What is the day today?":
        txt.insert(END, "\n" + "Bot => Today is " + datetime.datetime.now().strftime("%A"))
    elif e.get() == "ok" or e.get() == "OK":
        txt.insert(END, "\nBot => Thanks for your time............ ")
    elif e.get() == "What is the lesson of life?":
        txt.insert(END, "\n" + "Bot => Not to make the same mistake twice..!")
    elif e.get() == "Do you play song for me?":
        txt.insert(END, "\n" + "Bot => Yes, Why not..!!!!!!!!!")
        mixer.init()
        mixer.music.load("D:\SYNC Intern\ChatBot\Cheap Thrills.mp3")
        mixer.music.play(loops=1)
    elif e.get() == "Stop playing!":
        txt.insert(END, "\n" + "Bot => Ok..........!!!!")
        mixer.music.stop()
    elif e.get() == "Do you like Siri?":
        txt.insert(END, "\n" + "Bot => She seems clever..!")
    elif e.get() == "Who is your favourite person?":
        txt.insert(END, "\n" + "Bot => You're definitely a top contender for my favourite person!!!!")
    elif e.get() == "Am I a good person?":
        txt.insert(END, "\n" + "Bot => Well, I like you..!")
    elif e.get() == "Do you ever get hungry?":
        txt.insert(END, "\n" + "Bot => I'm always full of information....!")
    elif e.get() == "Do you sleep?":
        txt.insert(END, "\n" + "Bot => Sometimes I power down, which is a sort of like a nap..!!!!!!!!!!!!")
    e.delete(0, END)

#===================== Entry Fields============================

txt = Text(root,bg="black",fg="white")
txt.grid(row=0,column=0,columnspan=2)
e = Entry(root,bg="light blue",width=100)
e.grid(row=1,column=0)
Button(root,text="Send",command=send,bg="green",font=8).grid(row=1,column=1)

#================= Root Calling =========================


root.mainloop()
