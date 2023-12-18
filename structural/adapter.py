from abc import ABC, abstractmethod


class Audio(ABC):
    @abstractmethod
    def audioRecord(self):
        pass


class Midi(ABC):
    @abstractmethod
    def midiTrack(self):
        pass


class AudioTrack(Audio):
    def audioRecord(self):
        print('Audio is playing...')


class MidiTrack(Midi):
    def midiTrack(self):
        print('Midi is playing...')


class AudioToMidiAdapter(Audio):
    def __init__(self):
        self.midi = MidiTrack()

    def audioRecord(self):
        self.midi.midiTrack()