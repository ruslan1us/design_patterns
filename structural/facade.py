from pathlib import Path

class MP3:
    def process(self):
        print('Processing MP3...')
        Path('filename.mp3').touch()

class WAV:
    def process(self):
        print('Processing WAV...')
        Path('filename.wav').touch()

class Data:
    def process(self):
        print('Processing analysis. Making data...')
        Path('filename.data').touch()


class Render:
    def __init__(self):
        self.mp3 = MP3()
        self.wav = WAV()
        self.data = Data()

    def startRenderingAll(self):
        self.mp3.process()
        self.wav.process()
        self.data.process()

    def startRenderingMP3andWAV(self):
        self.mp3.process()
        self.wav.process()

    def startRenderingMP3(self):
        self.mp3.process()

    def startRenderingWAV(self):
        self.wav.process()

    def startRenderingData(self):
        self.data.process()