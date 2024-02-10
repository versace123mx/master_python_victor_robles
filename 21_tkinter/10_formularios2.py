from tkinter import *

ventana = Tk()
ventana.geometry("400x400")
ventana.title("Formularios 2")
ventana.config(bd=25)


encabezado = Label(ventana,text="Formualrios 2")
encabezado.config(padx=15,pady=15,fg='White',bg='green',font=("Arial",20))
encabezado.grid(row=0,column=0,columnspan=6,sticky=W)


def mostrarProfesion():
    texto = ""
    if web.get():
        texto += "Desarrollo web"
    
    if movil.get():
        if web.get():
            texto += " y Desarrollo movil"
        else:
            texto += "Desarrollo movil"

    mostrar.config(text=texto)


web = IntVar()
movil = IntVar()
#boton check
Label(ventana,text="Aque te dedicas").grid(row=1,column=0)
Checkbutton(ventana,text="Desarrollo web",variable=web,onvalue=1,offvalue=0,command=mostrarProfesion).grid(row=2,column=0)
Checkbutton(ventana,text="Desarrollo movil",variable=movil,onvalue=1,offvalue=0,command=mostrarProfesion).grid(row=3,column=0)

mostrar = Label(ventana,bg="green")
mostrar.grid(row=4,column=0)

#radio buttons

def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set("Masculino")
Label(ventana,text="¿Cual es tu genero?").grid(row=5)

Radiobutton(ventana,text="Masculino",value="Masculino",variable=opcion,command=marcar).grid(row=6)
Radiobutton(ventana,text="Femenino",value="Femenino",variable=opcion,command=marcar).grid(row=7)
marcado = Label(ventana)
marcado.grid(row=8)

#Menu de opcciones

def seleccionar():
    seleccionado.config(text=opccionSelect.get())

opccionSelect = StringVar()
opccionSelect.set("Opccion1")
Label(ventana,text="¿Cual es tu genero?").grid(row=5,column=1)
select = OptionMenu(ventana,opccionSelect,"Opccion1","Opccion2","Opccion3")
select.grid(row=6,column=1)

Button(ventana,text="Ver",command=seleccionar).grid(row=7,column=1)
seleccionado = Label(ventana)
seleccionado.grid(row=8,column=1)


ventana.mainloop()