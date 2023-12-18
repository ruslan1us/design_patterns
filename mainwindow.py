from tkinter import *

from creational.singleton import Singleton
import eqswindow
import footerwindow
import convertwindow
import decoratorwindow


class Window(Tk, Singleton):
    def init(self):
        super().__init__()
        self.button = Button(self, text='Open eqs window', command=self.create_window_eqs)
        self.button.pack(expand=True)

        self.button = Button(self, text='Open footer', command=self.create_footer)
        self.button.pack(expand=True)

        self.button = Button(self, text='Audio to midi', command=self.create_adapter)
        self.button.pack(expand=True)

        self.button = Button(self, text='decorator', command=self.create_decorator)
        self.button.pack(expand=True)

    def create_window_eqs(self):
        global extraWindow
        extraWindow = eqswindow.Extra()

    def create_footer(self):
        global extraWindow
        extraWindow = footerwindow.Extra()

    def create_adapter(self):
        global extraWindow
        extraWindow = convertwindow.Extra()

    def create_decorator(self):
        global extraWindow
        extraWindow = decoratorwindow.Extra()

    def __init__(self):
        print('calling from __init__')