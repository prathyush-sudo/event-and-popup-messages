from tkinter import *
from tkinter import messagebox

t=Tk()
t.geometry("400x400")

def msg():
    messagebox.showinfo("alert","stop virus found")
    
btn=Button(t,text="scan for viruses",command=msg)
btn.place(x=40,y=80)

t.mainloop()