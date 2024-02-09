class Coche:

    #atributos (variables)
    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2

    #Constructor
    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas


    #Metodos (funciones)
    def acelerar(self):
        self.velocidad +=1
    
    def frenar(self):
        self.velocidad -=1
    
    def cambiaColor(self,nuevocolor):
        self.color = nuevocolor

    def getVelocidad(self):
        return self.velocidad
    
    def getColor(self):
        return self.color
    