#!/usr/bin/python3
class Persona:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

          def presentation(self):
                    print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")

class Trabajador(Persona):
        def __init__(self, nombre, edad, departamento, puesto):
            super(Trabajador, self).__init__(nombre, edad)

            self.departamento = departamento
            self.puesto = puesto

per1 = Trabajador("Alberto", 22, "RRHH", "Becario")
per1.presentation()