from televisores.tv import TV


class Control:
    def __init__(self):
        self._tv = TV()

    def setCanal(self, canal):
        self._tv.setCanal(canal)

    def setVolumen(self, volumen):
        self._tv.setVolumen(volumen)

    def turnOn(self, estado):
        self._tv.turnOn(estado)

    def turnOff(self, estado):
        self._tv.turnOff(estado)

    def volumeUp(self):
        self._tv.volumeUp()

    def volumeDown(self):
        self._tv.volumeDown()

    def enlazar(self, televisor):
        self._tv = televisor
        televisor.setControl(self)
    def getTv(self):
        return self._tv

    def setTv(self, tv):
        self._tv = tv