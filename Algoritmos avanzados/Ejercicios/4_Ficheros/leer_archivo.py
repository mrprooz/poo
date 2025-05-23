with open ("archivo.txtx", "r") as fichero:
    for linea in fichero:
        linea = linea.strip()
        for caracter in linea:
            print(caracter)