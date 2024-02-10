from tkinter import *
import os.path


class Programa:

    def __init__(self):
        self.titulo = "Interface grafica con Python y Tkinter"
        self.icono = './imagenes/python_logo.ico'
        self.icono_alt = './21_tkinter/imagenes/python_logo.ico'
        self.size = "750x450"
        self.resizable = False


    def cargar(self):

        #Crear la ventana
        ventana = Tk()
        self.ventana = ventana #esto se declara para poder utilizar ventana en otros metodos

        #comprobar la ruta del fichero
        ruta_icono = os.path.abspath(self.icono)

        #mostrar texto en la ventna
        texto = Label(ventana,text=ruta_icono)
        texto.pack()

        #darle un tamaño a la ventana
        ventana.geometry(self.size)

        if self.resizable:
            #evitar que la venta se re ajuste
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)


        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icono_alt)

        #agregar icono
        ventana.iconbitmap(ruta_icono)


        #titulo de la ventana
        ventana.title(self.titulo)

        #arrancar y mostrar la venta
        #ventana.mainloop() lo quitamos de aqui para meterlo despues

    def addTexto(self,texto1):
        texto = Label(self.ventana,text=texto1)
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()
        

ventana = Programa()
ventana.cargar()
ventana.addTexto("Hola Venessita Culoncita")
ventana.mostrar()