#!/usr/bin/python3
import sys
class Persona:
        def __init__(self, nombre, edad): #la variable nombre contiene el valor que indiquemos al crear la instancia, una vez indicada en los parametros, perdemos su valor
            self.nombre = nombre #self.nombre contiene el valor que asignamos al crear la instancia al atributo nombre. Siempre estará accesible al acceder a los atributos de la instancia
            self.edad = edad

        def presentation(self):
                    print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")

class Trabajador(Persona):
        def __init__(self, nombre, edad, departamento = 'Data', puesto = 'Analist'):
            super(Trabajador, self).__init__(nombre, edad)

            self.departamento = departamento
            self.puesto = puesto
        def presentation(self):
            print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")
            print(f"Mi departamento es {self.departamento} y mi puesto es {self.puesto}")

trabajador_1 = Trabajador("Alberto", '22', "RRHH", "Becario")
trabajador_1.presentation()

my_var_list = ['Andrea', '42', 'Ventas', 'Manager']
trabajador_2 = Trabajador(my_var_list[0], my_var_list[1], my_var_list[2], my_var_list[3])
trabajador_2.presentation()

my_var_dict = {'nombre' : 'Andrea', 'edad' : '42', 'departamento': 'Ventas', 'puesto' : 'Manager'}
trabajador_3 = Trabajador(my_var_dict['nombre'], my_var_dict['edad'], my_var_dict['departamento'], my_var_dict['puesto'])
trabajador_3.presentation()
