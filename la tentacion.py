print(" ") # print imprime un espacio
print("Sanchez Perez briana Sarahi, 1213, 3W")
print(" ") # print imprime un espacio

import os # permite eliminar el archivo
if os.path.exists("papa.txt"): # se busca el archivo seleccionado
  os.remove("papa.txt") # se elimina el archivo seleccionado
else: # se ejecuta si no se encuentra el archivo
  print("The file does not exist") # print imprime si no se encuentra el archivo

print(" ") # print imprime un espacio