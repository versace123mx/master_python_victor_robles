from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry("400x400")
ventana.title("Calculadora")
ventana.config(bd=25)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()


def sumar():
    res = validaTypo(numero1.get(),numero2.get())
    ejecutaAccion(res,'sumar')

def restar():
    res = validaTypo(numero1.get(),numero2.get())
    ejecutaAccion(res,'restar')

def multiplicar():
    res = validaTypo(numero1.get(),numero2.get())
    ejecutaAccion(res,'multiplicar')

def dividir():
    res = validaTypo(numero1.get(),numero2.get())
    ejecutaAccion(res,'dividir')

def mostrarResultado():
    MessageBox.showinfo("Resultado",f"El resultado de la operacion es {resultado.get()}")
    numero1.set('')
    numero2.set('')

def validaTypo(var1,var2):
    msj = False
    if var1.isnumeric() and var2.isnumeric():
        msj=True
    
    return msj
    

def muestraError():
    MessageBox.showerror("error",f"Los valores deben de ser numeros")
    numero1.set('')
    numero2.set('')

def ejecutaAccion(resp,operacion):
    if resp:
        if operacion == 'sumar':
            op = float(numero1.get()) + float(numero2.get())
        elif operacion == 'restar':
            op = float(numero1.get()) - float(numero2.get())
        elif operacion == 'multiplicar':
            op = float(numero1.get()) * float(numero2.get())
        elif operacion == 'dividir':
            op = float(numero1.get()) / float(numero2.get())

        resultado.set(op)
        mostrarResultado()
    else:
        muestraError()

marco = Frame(ventana,width=300,height=200)
marco.config(bd=5,relief=SOLID,padx=15,pady=15)
marco.pack(side=TOP,anchor=CENTER)
marco.pack_propagate(False)

Label(marco,text="Primer numero").pack()
Entry(marco,textvariable=numero1).pack()

Label(marco,text="Segundo numero").pack()
Entry(marco,textvariable=numero2).pack()


Label(marco,text='').pack()
Button(marco,text="Sumar",command=sumar).pack(side="left",fill=X,expand=YES)
Button(marco,text="Restar",command=restar).pack(side="left",fill=X,expand=YES)
Button(marco,text="Multiplicar",command=multiplicar).pack(side="left",fill=X,expand=YES)
Button(marco,text="Dividir",command=dividir).pack(side="left",fill=X,expand=YES)

ventana.mainloop()