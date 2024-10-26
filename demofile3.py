print(" ") # print imprime un espacio
print("Martinez Tagle Luis Angel 3w 1196")#imprime el nombre del programador y  el numero de control 
print(" ") # print imprime un espacio

f = open("demofile3.txt", "w") # abriendo mi archivo de texo para solo en escribir
f.write("Woops! I have deleted the content!") # se escribe un texto 
f.close() # se cierra el archivo

f = open("demofile3.txt", "r") # abro mi archivo de texo para solo en lectura
print(f.read()) # lee mi archivo

print(" ") # print imprime un espacio

