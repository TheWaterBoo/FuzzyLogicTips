import functions as fn

#Se obtiene la membresia de la comida con trapezoide
class FoodQuality:
    def __init__(self, foodQuality):
        self.desagradable = 0
        self.aceptable = 0
        self.delicioso = 0
        if 0 <= foodQuality <= 10:
            self.desagradable = fn.funcionMembresiaTrapezoidal(1,1,3,5, foodQuality)
            self.aceptable = fn.funcionMembresiaTrapezoidal(4,5,7,8, foodQuality)
            self.delicioso = fn.funcionMembresiaTrapezoidal(7,8.5,10,10,foodQuality)