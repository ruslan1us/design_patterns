from tkinter import *
from tkinter.messagebox import askquestion
from structural.facade import *

class Extra(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Rendering window')
        self.geometry('400x400')
        self.mp3 = IntVar(value=0)
        self.wav = IntVar(value=0)
        self.data = IntVar(value=0)

        first_check_box = Checkbutton(self, text='MP3', variable=self.mp3, command=self.start_rendering)
        first_check_box.pack()
        second_check_box = Checkbutton(self, text='WAV', variable=self.wav, command=self.start_rendering)
        second_check_box.pack()
        third_check_box = Checkbutton(self, text='Data', variable=self.data, command=self.start_rendering)
        third_check_box.pack()
        self.button = Button(self, text='Render all', command=self.start_rendering)
        self.button.pack(expand=True)

    def start_rendering(self):
        askquestion('...', message='Start rendering?')
        renderTrack = Render()
        if self.mp3.get() and not self.wav.get() and not self.data.get():
            renderTrack.startRenderingMP3()
        elif not self.mp3.get() and self.wav.get() and not self.data.get():
            renderTrack.startRenderingWAV()
        elif not self.mp3.get() and not self.wav.get() and self.data.get():
            renderTrack.startRenderingData()
        else:
            renderTrack.startRenderingAll()
