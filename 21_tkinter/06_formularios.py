from tkinter import *

ventana = Tk()
ventana.geometry("900x700")
ventana.title("Formularios")

#Texto de encabezado
encabezado = Label(ventana,text="Formularios con Tkinter")
encabezado.config(fg="white",bg="darkgray",font=("Open Sans",18),padx=10,pady=10)
encabezado.grid(row=0,column=0,columnspan=12,sticky=N)


#label para el campo
Label(ventana,text="Nombre:").grid(row=1,column=0)

#campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=1,column=1,padx=5,pady=5,sticky=N)

#label para el campo
Label(ventana,text="Apellidos:").grid(row=2,column=0)

#campo de texto
campo_texto = Entry(ventana)
campo_texto.grid(row=2,column=1,padx=5,pady=5,sticky=N)
campo_texto.config(state="disabled")

#tex area 
#label para el campo
Label(ventana,text="Apellidos:").grid(row=3,column=0,sticky=N,padx=5,pady=5)
text_area = Text(ventana)
text_area.grid(row=3, column=1)
text_area.config(width=30,height=5,padx=15,pady=15)


#boton
Label(ventana).grid(row=4,column=1)
boton = Button(ventana,text="Enviar")
boton.grid(row=5,column=1,sticky=W)
boton.config(padx=10,pady=10,bg="green",fg="white")


ventana.mainloop()