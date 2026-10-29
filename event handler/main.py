from tkinter import *

t=Tk()
t.title("event handler ")
t.geometry("200x200")

def handle_keypress(event):
    print("Key pressed:", event.char)

t.bind("<Key>", handle_keypress)

def handle_click(event):
    print("clicked")

btn=Button(text="click me")
btn.pack()
btn.bind("<Button-1>", handle_click)

t.mainloop()