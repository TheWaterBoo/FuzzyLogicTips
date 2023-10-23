import functions as fn

#Se obtiene la membresia del servicio con trapezoidal
class ServiceQuality:
    def __init__(self, serviceQuality):
        self.pesimo = 0
        self.promedio = 0
        self.excelente = 0
        if 0 <= serviceQuality <= 10:
            self.pesimo = fn.funcionMembresiaTrapezoidal(1,1,3,4,serviceQuality)
            self.promedio = fn.funcionMembresiaTrapezoidal(3,4,7,8,serviceQuality)
            self.excelente = fn.funcionMembresiaTrapezoidal(7,9,10,10,serviceQuality)