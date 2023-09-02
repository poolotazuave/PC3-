#EJERCICIO NUMERO 5 DE PC3
class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []
    
    def display(self):
        print("Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print("Notas:")
            for i, nota in enumerate(self.notas, start=1):
                print(f"Nota {i}: {nota}")
    
    def setAge(self, edad):
        self.edad = edad
    
    def setNota(self, notas):
        self.notas = notas

# Ejemplo 
nombre = input("Ingrese el nombre del estudiante: ")
numero_registro = input("Ingrese el número de registro del estudiante: ")

alumno = Alumno(nombre, numero_registro)

# Asignar edad al estudiante
edad = int(input("Ingrese la edad del estudiante: "))
alumno.setAge(edad)

# Asignar notas al estudiante
notas = []
num_notas = int(input("Ingrese la cantidad de notas a asignar: "))
for i in range(num_notas):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)
alumno.setNota(notas)

# Mostrar información del estudiante
alumno.display()
