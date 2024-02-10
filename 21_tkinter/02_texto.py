from tkinter import *

ventana = Tk()
ventana.geometry("500x500")


texto = Label(ventana,text="Bienvenido a mi programa")
texto.config(fg="yellow",bg="black",padx=20,pady=40,font=("Arial",30))
texto.pack()


texto2 = Label(ventana,text="Soy otro texto")
texto2.pack(anchor=E)

ventana.mainloop()