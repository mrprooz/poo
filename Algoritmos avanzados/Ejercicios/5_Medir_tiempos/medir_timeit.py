import timeit

def algoritmo():
    
    suma= sum (range (100))
    
tiempo_promedio = tiemeit.timeit(algoritmo, number=1000) / 1000

print(f"Tiempo promedio: {tiempo_promedio} segundos")