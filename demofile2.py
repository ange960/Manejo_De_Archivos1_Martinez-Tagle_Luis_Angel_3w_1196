print(" ") # print imprime un espacio
print("Martinez Tagle Luis Angel 3w 1196")#imprime el nombre del programador y  el numero de control 
print(" ") # print imprime un espacio


f = open("demofile2.txt", "a") # abro mi archivo de texo para solo en anexar
f.write("Now the file has more content!") # escribe un texto
f.close() # se ciera mi archivo

f = open("demofile2.txt", "r") # abro mi archivo de texo para solo en lectura
print(f.read()) # lee mi archivo

print(" ") # print imprime un espacio


