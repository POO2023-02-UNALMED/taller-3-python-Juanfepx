class TV:
    _numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV._numTV += 1

    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca

    def getCanal(self):
        return self._canal

    def setCanal(self, canal):
        if 1 <= self._canal <= 120 and self._estado:
            self._canal = canal

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self._precio = precio

    def getVolumen(self):
        return self._volumen

    def setVolumen(self, volumen):
        if 0 <= self._volumen <= 7 and self._estado:
            self._volumen = volumen

    def getControl(self):
        return self._control

    def setControl(self, control):
        self._control = control

    def getNumTV(self):
        return self._numTV

    def setNumTV(self, numTV):
        self._numTV = numTV

    def turnOn(self, estado):
        self._estado = True

    def turnOff(self, estado):
        self._estado = False

    def getEstado(self):
        return self._estado

    def canalUp(self):
        if self._canal < 120 and self._estado:
            self._canal += 1

    def canalDown(self):
        if self._canal > 1 and self._estado:
            self._canal -= 1

    def volumeUp(self):
        if self._volumen < 7 and self._estado:
            self._volumen += 1

    def volumeDown(self):
        if self._volumen > 0 and self._estado:
            self._volumen -= 1
