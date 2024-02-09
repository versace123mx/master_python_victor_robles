from io import open
import pathlib
import shutil
#abrir archivo
#archivo = open('fichero_texto.txt','a+')
ruta = str(pathlib.Path().absolute())+'\\fichero_texto.txt'
archivo = open(ruta,'a+')

#escribir en el archivo
archivo.write("SOy un texto")

#cerrar archivo
archivo.close()

#copiar archivo de una ruta a otra ruta
rutaNueva = str(pathlib.Path().absolute().parent)+"/fichero_texto_copiado.txt" #nueva ruta
rutaNueva2 = str(pathlib.Path().absolute()) +"/../fichero_texto_copiado_2.txt" #nueva ruta
rutaNueva3 = str(pathlib.Path().absolute()) +"/../../fichero_texto_copiado_3.txt" #nueva ruta
#print(rutaNueva)
#print(rutaNueva2)
shutil.copyfile(ruta,rutaNueva)
shutil.copyfile(ruta,rutaNueva2)
shutil.copyfile(ruta,rutaNueva3)