from functools import reduce
numeros=[1,2,3,4,5,6]

resultado= reduce(lambda a, b: a+b if % 2==0 else a, numeros, 0)

print(resultado)