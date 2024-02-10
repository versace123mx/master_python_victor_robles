from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("900x700")

imagen = Image.open("./21_tkinter/imagenes/python_logo_a.png")
render = ImageTk.PhotoImage(imagen)
Label(ventana,image=render).pack()


ventana.mainloop()