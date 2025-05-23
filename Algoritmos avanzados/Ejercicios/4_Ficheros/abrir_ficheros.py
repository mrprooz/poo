#Forma "mala"
fichero = open ("fichero.txt", "r")
contenido = fichero.read()
print(contenido)
fichero.close


#Forma moderna pro
with open ("fichero.txt", "r") as fichero:
    contenido = fichero.read()
    print(contenido)