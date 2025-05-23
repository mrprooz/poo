# clase nodo, representa cada elemento de la lista enlazada
class Nodo:
    def __init__(self, dato):
        self.dato = dato        # El valor es almacenado en el nodo
        self.siguiente = None   # Referencia el siguiente nodo

# Clase ListaEnlazada: contiene operaciones típicas de una lista
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None      # Puntero al primer nodo de la lista
        self._longitud = 0      # Contador de elementos en la lista

    # Crea una lista vacía (reinicia la lista)
    def Crear(self):
        self.cabeza = None
        self._longitud = 0

    # Inserta un nuevo elemento 'e' en la posición 'p'
    def Insertar(self, e, p):
        if p < 0 or p > self._longitud:
            raise IndexError("Índice fuera de rango")

        nuevo = Nodo(e)  # Creamos el nuevo nodo con el valor e

        if p == 0:
            # Insertar al principio de la lista
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            # Insertar en una posición intermedia o al final
            anterior = self._nodo_en(p - 1)
            nuevo.siguiente = anterior.siguiente
            anterior.siguiente = nuevo

        self._longitud += 1  # Aumentamos la longitud

    # Elimina el nodo en la posición 'p'
    def Eliminar(self, p):
        if p < 0 or p >= self._longitud:
            raise IndexError("Índice fuera de rango")

        if p == 0:
            # Eliminar el primer nodo
            self.cabeza = self.cabeza.siguiente
        else:
            # Eliminar un nodo intermedio o final
            anterior = self._nodo_en(p - 1)
            anterior.siguiente = anterior.siguiente.siguiente

        self._longitud -= 1  # Reducimos la longitud

    # Busca el valor 'e' en la lista y devuelve su posición (o -1 si no se encuentra)
    def Buscar(self, e):
        actual = self.cabeza
        indice = 0

        # Recorremos la lista
        while actual:
            if actual.dato == e:
                return indice
            actual = actual.siguiente
            indice += 1

        return -1  # No se encontró

    # Obtiene el elemento que está en la posición 'p'
    def Obtener(self, p):
        if p < 0 or p >= self._longitud:
            raise IndexError("Índice fuera de rango")
        return self._nodo_en(p).dato

    # Devuelve el número de elementos en la lista
    def Longitud(self):
        return self._longitud

    # Verifica si la lista está vacía
    def EsVacía(self):
        return self._longitud == 0

    # Actualiza el valor en la posición 'p' con el nuevo valor 'e'
    def Actualizar(self, p, e):
        if p < 0 or p >= self._longitud:
            raise IndexError("Índice fuera de rango")
        self._nodo_en(p).dato = e

    # Función auxiliar privada para obtener el nodo en la posición 'p'
    def _nodo_en(self, p):
        actual = self.cabeza
        for _ in range(p):
            actual = actual.siguiente
        return actual

    # Método opcional para imprimir la lista como una cadena
    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "[" + ", ".join(elementos) + "]"
    
L = ListaEnlazada()
L.Insertar(10, 0)   # [10]
L.Insertar(20, 1)   # [10, 20]
L.Insertar(15, 1)   # [10, 15, 20]
print(L)            # [10, 15, 20]
L.Eliminar(1)       # [10, 20]
print(L.Obtener(1)) # 20
print(L.Buscar(10)) # 0
print(L.Longitud()) # 2
print(L.EsVacía())  # False
L.Actualizar(0, 99) # [99, 20]
print(L)            # [99, 20]

