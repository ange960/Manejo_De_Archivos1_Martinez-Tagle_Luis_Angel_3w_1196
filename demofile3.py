print(" ") # print imprime un espacio
print("Sanchez Perez briana Sarahi, 1213, 3W")
print(" ") # print imprime un espacio

f = open("demofile3.txt", "w") # abriendo mi archivo de texo para solo en escribir
f.write("Woops! I have deleted the content!") # se escribe un texto 
f.close() # se cierra el archivo

f = open("demofile3.txt", "r") # abro mi archivo de texo para solo en lectura
print(f.read()) # lee mi archivo

print(" ") # print imprime un espacio

