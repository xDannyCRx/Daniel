class Punto:
    def __init__(self, x=0, x=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return "x:{}, y: {}".formt(self.x, self.y)
 #$Y ahora queremos anadir una Clase Circulo que herede de Punto. Para conocer todos los deta
 class Circulo(Punto):
     def __init__(self, radio, *args, **kwargs):
         self.radio = radio
        super().__init__(*args, **Kwargs)
    def __repr_(self):
        return "x: {}, y:{}, radio: {}".format(self.x, self.y, self.radio)
