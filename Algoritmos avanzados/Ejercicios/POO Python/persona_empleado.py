class Persona:
    def saludar (self):
        print("Hola, soy una persona")
        
class Empleado(Persona):
    def saludar(self):
        print("Hola, soy un empleado")
        
p = Persona()
e = Empleado()

tupla=(e,p)

for i in tupla:
    i.saludar()