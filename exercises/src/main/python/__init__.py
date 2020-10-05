#!/usr/bin/python3
import sys
class Persona:
        def __init__(self, nombre, edad): #la variable nombre contiene el valor que indiquemos al crear la instancia, una vez indicada en los parametros, perdemos su valor
            self.nombre = nombre #self.nombre contiene el valor que asignamos al crear la instancia al atributo nombre. Siempre estará accesible al acceder a los atributos de la instancia
            self.edad = edad

          def presentation(self):
                    print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")

class Trabajador(Persona):
        def __init__(self, nombre, edad, departamento, puesto):
            super(Trabajador, self).__init__(nombre, edad)

            self.departamento = departamento
            self.puesto = puesto
        def presentation(self):
            print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")
            print(f"Mi departamento es {self.departamento} y mi puesto es {self.puesto}")

trabajador_1 = Trabajador("Alberto", 22, "RRHH", "Becario")
trabajador_1.presentation()