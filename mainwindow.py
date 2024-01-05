from tkinter import *

import renderwindow
from creational.singleton import Singleton
import eqswindow
import footerwindow
import convertwindow
import decoratorwindow
import iteratorwindow
import groupwindow
import strategywindow


class Window(Tk, Singleton):
    def init(self):
        super().__init__()
        self.button = Button(self, text='Open eqs window', command=self.create_window_eqs)
        self.button.pack(expand=True)

        self.button = Button(self, text='Open footer', command=self.create_footer)
        self.button.pack(expand=True)

        self.button = Button(self, text='Audio to midi', command=self.create_adapter)
        self.button.pack(expand=True)

        self.button = Button(self, text='Decorator', command=self.create_decorator)
        self.button.pack(expand=True)

        self.button = Button(self, text='Export', command=self.create_export_window)
        self.button.pack(expand=True)

        self.button = Button(self, text='Search', command=self.create_iterator_window)
        self.button.pack(expand=True)

        self.button = Button(self, text='Group', command=self.create_group_window)
        self.button.pack(expand=True)

        self.button = Button(self, text='Strategy', command=self.create_strategy_window)
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

    def create_export_window(self):
        global extraWindow
        extraWindow = renderwindow.Extra()

    def create_iterator_window(self):
        global extraWindow
        extraWindow = iteratorwindow.Extra()

    def create_group_window(self):
        global extraWindow
        extraWindow = groupwindow.Extra()

    def create_strategy_window(self):
        global extraWindow
        extraWindow = strategywindow.Extra()

    def __init__(self):
        print('calling from __init__')