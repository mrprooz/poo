palabras= ["manzana", "banana", "cereza", "uva"]

filtro_vocal = list(filter(lambda x: x[0].lower() in "aeiou", palabras))

print(filtro_vocal)