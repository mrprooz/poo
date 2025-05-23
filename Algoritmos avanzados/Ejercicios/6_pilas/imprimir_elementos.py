from queue import LifoQueue

mi_pila = LifoQueue()
print(mi_pila)
mi_pila.put(1)
mi_pila.put(2)
mi_pila.put(3)
print(f"tamalo={mi_pila.qsize()}")

elem = mi_pila.get()
print(f"elemento={elem}")
elem = mi_pila.get()
print(f"elemento={elem}")
elem = mi_pila.get(block=true, timeout=5)
print(f"elemento={elem}")