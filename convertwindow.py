from tkinter import Toplevel, Button
from structural.adapter import *


class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Convert window')
        self.geometry('640x480')

        self.button = Button(self, text='Audio Record', command=self.audio)
        self.button.pack(expand=True)

        self.button = Button(self, text='Midi', command=self.midi)
        self.button.pack(expand=True)


    def audio(self):
        track = AudioTrack()
        track.audioRecord()

    def midi(self):
        track = AudioToMidiAdapter()
        track.audioRecord()