from tkinter import *
from structural.decorator import *


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Decorator window')
        self.geometry('640x480')
        self.dry = Entity('sound')

        self.l = Label(self, bg='white', width=30, text=self.dry.play())
        self.l.pack()

        self.comp = IntVar(value=0)
        self.eq = IntVar(value=0)
        first_check_box = Checkbutton(self, text='Compressor', variable=self.comp, command=self.result)
        first_check_box.pack()
        second_check_box = Checkbutton(self, text='EQ', variable=self.eq, command=self.result)
        second_check_box.pack()


    def result(self):
        if (self.comp.get()) and (not self.eq.get()):
            wet = Compressor(self.dry)
            self.l.config(text=wet.play())
        elif (not self.comp.get()) and (self.eq.get()):
            wet = EQ(self.dry)
            self.l.config(text=wet.play())
        elif (self.comp.get()) and (self.eq.get()):
            wet = EQ(Compressor(self.dry))
            self.l.config(text=wet.play())
        else:
            self.l.config(text=self.dry.play())
