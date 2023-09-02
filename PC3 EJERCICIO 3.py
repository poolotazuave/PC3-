#EJERCCIO NUMERO 3 DE PC3
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return area

# Ejemplo 
radio = float(input("Ingrese el radio del círculo: "))
circulo = Circulo(radio)
area = circulo.calcular_area()
print(f"El área del círculo con radio {radio} es {area:.2f}")
