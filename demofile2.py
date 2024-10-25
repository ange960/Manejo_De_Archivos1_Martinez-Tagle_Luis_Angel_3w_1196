print(" ") # print imprime un espacio
print("Sanchez Perez briana Sarahi, 1213, 3W")
print(" ") # print imprime un espacio


f = open("demofile2.txt", "a") # abro mi archivo de texo para solo en anexar
f.write("Now the file has more content!") # escribe un texto
f.close() # se ciera mi archivo

f = open("demofile2.txt", "r") # abro mi archivo de texo para solo en lectura
print(f.read()) # lee mi archivo

print(" ") # print imprime un espacio


