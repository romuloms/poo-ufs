from tkinter import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.msg = Label(self, text="Hello world")
        self.msg.pack()
        self.bye = Button(self, text="Close", command=self.quit)
        self.bye.pack()
        self.pack()

app = App()
mainloop()