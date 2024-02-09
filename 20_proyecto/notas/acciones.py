import notas.nota as modelo

class Acciones:

    def crear(self,usuario):
        print(f"Ok {usuario[1]}!! Vamos a crear una nueva nota.....")
        titulo = input("Intoduce el titulo de tu nota: ")
        descripccion = input("Mete el contenido de tu nota:")
        nota = modelo.Nota(usuario[0],titulo,descripccion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"Perfecto haz guardado la nota: {titulo}")
        else:
            print(f"No se ha podido guardar la nota, lo siento {usuario[1]}")
    
    def mostrar(self,usuario):
        print(f"\nVale {usuario[1]}!! Aqui tienes tus notas: \n")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        if len(notas) >= 1:
            for nota in notas:
                print(f"idNota: {nota[0]} - TituloNota: {nota[3]}")
        else:
            print("Aun no tienes notas ;(")
        

    def borrar(self,usuario):
        print(f"\nOk {usuario[1]}!! Vamos a borrar notas:\n")
        id = input("Introduce el id de la nota a borrar: ")
        nota = modelo.Nota(usuario[0])
        borrar = nota.eliminar(id)
        if isinstance(borrar[0], int):
            print(f"El registro ha sido eliminado correctamente :) !!\n")
        else:
            print(f"{borrar[0]}")