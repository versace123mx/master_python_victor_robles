class Coche:

    #atributos (variables)
    color = 'Rojo'
    marca = 'Ferrari'
    modelo = 'Aventador'
    velocidad = 300
    caballaje = 500
    plazas = 2

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
    
    def prueba(self):
        print( "hola mundo")

coche1 = Coche()
print(f"La velocidad inicial del coche es: {coche1.velocidad}")
coche1.acelerar()
coche1.acelerar()
print(f"Acelere el coche dos veces ahora su valor es: {coche1.getVelocidad()}")
print(f"Color inicial: {coche1.color}")
coche1.cambiaColor('Blue')
print(f"Nuevo color: {coche1.getColor()}")
coche1.prueba()