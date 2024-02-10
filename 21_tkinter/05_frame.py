from tkinter import *

ventana = Tk()
ventana.title("Marcos en python")
ventana.geometry("700x700")

marcopadre = Frame(ventana,width=250,height=250)
marcopadre.config(bg="lightblue")
marcopadre.pack(side=TOP,anchor=N,fill=X,expand=YES)

marco = Frame(marcopadre,width=250,height=250)
marco.config(bg="red",bd=15,relief="solid")
marco.pack(side=LEFT,anchor=NW)
marco.pack_propagate(False)
texto = Label(marco,text="Texto 1")
texto.config(
    height=3,
    bg="orange",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT,fill=X,expand=YES)

marco = Frame(marcopadre,width=250,height=250)
marco.config(bg="blue",bd=15,relief="solid")
marco.pack(side=RIGHT,anchor=NE)
marco.pack_propagate(False)
texto = Label(marco,text="Texto 2")
texto.config(
    height=3,
    bg="orange",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT,fill=X,expand=YES)

marcopadre = Frame(ventana,width=250,height=250)
marcopadre.config(bg="lightblue")
marcopadre.pack(side=BOTTOM,anchor=S,fill=X,expand=YES)

marco = Frame(marcopadre,width=250,height=250)
marco.config(bg="green",bd=15,relief="solid")
marco.pack(side=LEFT,anchor=SW)
marco.pack_propagate(False)
texto = Label(marco,text="Texto 3")
texto.config(
    height=3,
    bg="orange",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT,fill=X,expand=YES)
marco = Frame(marcopadre,width=250,height=250)
marco.config(bg="pink",bd=15,relief="solid")
marco.pack(side=RIGHT,anchor=SE)
marco.pack_propagate(False)
texto = Label(marco,text="Texto 4")
texto.config(
    height=3,
    bg="orange",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT,fill=X,expand=YES)

ventana.mainloop()