#EJERCICIO NUMERO 4 DE PC3
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

# Ejemplo 
largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

rectangulo = Rectangulo(largo, ancho)
area = rectangulo.calcular_area()

print(f"El área del rectángulo con largo {largo} y ancho {ancho} es {area:.2f}")
