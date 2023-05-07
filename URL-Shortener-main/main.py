from tkinter import *
import pyshorteners

#======================= GUI Interface=================

root = Tk()
root.title("URL Shortener")
root.geometry("650x300")
root.resizable(False,False)

#========================== Shortening URL Function===========


def my_url():
    url_entry = url.get()
    result = pyshorteners.Shortener().tinyurl.short(url_entry)
    urlEntry.insert(END, result)

#============= Title ==============================

Label(root,text="Generate Short URL",font=("georgia",20,"bold"),fg="black").pack(pady=10)

#============================= Input URL ===============================

frame1 = Frame(root)
Label(frame1,text="Paste/Type Url Here: ",font=("georgia",15,"bold")).pack(side=LEFT)
url = Entry(frame1,width=35,font=("cambria",15),bg="light blue")
url.pack()
frame1.pack(pady=10)

#======================= Generate URL Button ============================

Button(root,text="Generate Link",font=("cambria",15,"bold"),fg="green",bg="light green",command=my_url).pack(pady=10)

#================== Output of Short URL =================================

frame2 = Frame(root)
Label(frame2,text="Copy URL: ",font=("georgia",15,"bold")).pack(side=LEFT)
urlEntry = Entry(frame2,width=35,font=("cambria",15,"bold"),bg="light blue")
urlEntry.pack()
frame2.pack(pady=10)

#========================== Display =============================
root.mainloop()