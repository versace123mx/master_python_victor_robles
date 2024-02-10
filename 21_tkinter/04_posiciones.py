from tkinter import *

ventana = Tk()
ventana.geometry("500x500")


texto = Label(ventana,text="Bienvenido a mi programa")
texto.config(fg="yellow",bg="black",padx=20,pady=40,font=("Arial",30))
texto.pack()


texto = Label(ventana,text="Texto 1")
texto.config(
    height=3,
    bg="orange",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT,fill=X,expand=YES)

texto = Label(ventana,text="Texto 2")
texto.config(
    height=3,
    bg="green",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT,fill=X,expand=YES)
texto = Label(ventana,text="Texto 3")
texto.config(
    height=3,
    bg="red",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT,fill=X,expand=YES)

ventana.mainloop()