from tkinter import *

ventana = Tk()
ventana.geometry("900x700")
ventana.title("Formularios")

def getdato():
    resultado.set(dato.get())

dato = StringVar()
resultado = StringVar()

Label(ventana,text="Mete un texto").pack(anchor=NW)
Entry(ventana,textvariable=dato).pack(anchor=NW)

Label(ventana,text="dato recogido").pack(anchor=NW)
Label(ventana,textvariable=resultado).pack(anchor=NW)


Button(ventana,text="Mostrar datos",command=getdato).pack(anchor=NW)

ventana.mainloop()