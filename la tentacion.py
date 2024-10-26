print(" ") # print imprime un espacio
print("Martinez Tagle Luis Angel 3w 1196")#imprime el nombre del programador y  el numero de control 
print(" ") # print imprime un espacio

import os # permite eliminar el archivo
if os.path.exists("papa.txt"): # se busca el archivo seleccionado
  os.remove("papa.txt") # se elimina el archivo seleccionado
else: # se ejecuta si no se encuentra el archivo
  print("The file does not exist") # print imprime si no se encuentra el archivo

print(" ") # print imprime un espacio
