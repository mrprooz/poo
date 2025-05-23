def contar_peldaños(escalera):
    if not escalera:
        return 0
    else:
        return 1 + contar_peldaños(escalera[1:])
    
escalera = ["escalon1", "escalon2", "escalon3", "escalon4"]
print(contar_peldaños(escalera))  # imprime 5