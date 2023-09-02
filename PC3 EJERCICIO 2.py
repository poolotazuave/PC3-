#EJERCICIO NUMERO DE 2 DE PC3
def obtener_calificaciones():
    while True:
        try:
            # Solicitar al usuario una lista de calificaciones separadas por comas
            calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
            
            # Dividir la cadena en calificaciones individuales y convertirlas en enteros
            calificaciones = [int(cal) for cal in calificaciones_str.split(',')]
            
            # Mostrar las calificaciones convertidas
            print("Calificaciones:", calificaciones)
            
            # Salir del bucle
            break
        
        except ValueError:
            print("Error: Asegúrese de ingresar calificaciones válidas (números enteros separados por comas).")
            continue

obtener_calificaciones()
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        try:
            # Calcular el área del círculo utilizando el atributo radio
            area = math.pi * (self.radio ** 2)
            return area
        
        except TypeError:
            print("Error: El radio debe ser un valor numérico.")

# Ejemplo
try:
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = Circulo(radio)
    area = circulo.calcular_area()
    print(f"El área del círculo con radio {radio} es {area:.2f}")
except ValueError:
    print("Error: Ingrese un valor numérico para el radio.")
