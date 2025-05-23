import time
def algortimo_1():
     total=0
     for i in range (1, 1000):
         for j in range (1,1000):
             total += i*j
             
def algoritmo_2():
    total= sum (i+j for  i in range(1,1000) for j in range(1,1000))
    
#funcion medir tiempo
def medir_tiempo(funcion):
    start_time= time.time()
    funcion()
    end_time=time.time()
    print(f"{func.__name__} tomó {end_time - start_time:.2f} segundos")
    
#conparar algoritmos

medir_tiempo(algortimo_1)
medir_tiempo(algortimo_2)