from tkinter import *

ventana = Tk()
ventana.geometry("400x400")
ventana.title("Formularios 2")
ventana.config(bd=25)

mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

archivo = Menu(mi_menu,tearoff=0)
archivo.add_command(label="New File")
archivo.add_command(label="New Window")
archivo.add_separator()
archivo.add_command(label="Open File")
archivo.add_command(label="Open Window")
archivo.add_separator()
archivo.add_command(label="Exit",command=ventana.quit)

mi_menu.add_cascade(label="Archivo",menu=archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Seleccion")
mi_menu.add_command(label="Help")

ventana.mainloop()