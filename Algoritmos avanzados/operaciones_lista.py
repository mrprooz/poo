lista_numeros=[]
num=int(input("Introduce los numeros para mostrar el mayor, el menor, la suma y la multiplicacion de ellos"))
lista_numeros.append(num)

decision=int(input("Quieres insertar mas? 1 si, 0 si no"))

while (decision==1):
    num=int(input("Introduce los numeros para mostrar el mayor, el menor, la suma y la multiplicacion de ellos"))
    lista_numeros.append(num)
    decision=int(input("Quieres insertar mas? 1 si, 0 si no"))
    
def mostrar_mayor(lista_numeros):
    return max(lista_numeros)

def mostrar_menor(lista_numeros):
    return min(lista_numeros)

def mostrar_suma(lista_numeros):
    return sum(lista_numeros)

def mostrar_multiplicacion(lista_numeros):
    multiplicacion=1
    for i in lista_numeros:
        multiplicacion= multiplicacion*i
        return multiplicacion
    

print(mostrar_mayor(lista_numeros))

print(mostrar_menor(lista_numeros))

print(mostrar_multiplicacion(lista_numeros))

print(mostrar_suma(lista_numeros))