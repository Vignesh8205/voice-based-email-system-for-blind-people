from tkinter import *
frame=Tk()
frame.geometry('300x300')
def test():
    id=1234
    e.insert(END,id)

e=Entry(frame,width='20')
e.place(x='50',y='50')
test()
# test()
frame.mainloop()