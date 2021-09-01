from tkinter import *

class JavaButton(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        stopper = Button(self, text='i know you', command=self.quit)
        stopper.back()
        stopper.config(bg='yellow', fg='blue', bd=15)

if __init__ == '__main__':
    JavaButton().mainloop()