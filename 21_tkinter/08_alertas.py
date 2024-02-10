from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry("900x700")
ventana.title("Alertas")
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showinfo("Alerta","Vanessita Culoncita")


def salir(nombre):
    resultado = MessageBox.askquestion("Salir","¿Realmente quieres salir?")
    if resultado == 'yes':
        MessageBox.showinfo("Alerta",f"Adios {nombre}")
        ventana.destroy()

Button(ventana,text="Mostrar Alerta",command=sacarAlerta).pack()


Button(ventana,text="salir",command=lambda:salir('Vanessita Culoncita')).pack()

ventana.mainloop()