class EQsFactory:
    def __init__(self):
        self._eqsfactory = [FabFilter(5, 'Pro Q3'), Waves(4,'WavesEQ'),
                            FruityParametricEQ(7, 'EQ2')]

    @property
    def eqs(self):
        return self._eqsfactory

class EQ:
    def __init__(self, bands, name):
        self.bands = bands
        self.name = name

    def getBands(self):
        return self.bands


class FabFilter(EQ):
    def __init__(self, bands, name):
        super().__init__(bands, name)

    def getBands(self):
        return super().getBands()


class Waves(EQ):
    def __init__(self, bands, name):
        super().__init__(bands, name)

    def getBands(self):
        return super().getBands()


class FruityParametricEQ(EQ):
    def __init__(self, bands, name):
        super().__init__(bands, name)

    def getBands(self):
        return super().getBands()