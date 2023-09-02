#EJERCICIO NUMERO 8 DE PC3
def suma(a, b):
    try:
        resultado = a + b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def resta(a, b):
    try:
        resultado = a - b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def producto(a, b):
    try:
        resultado = a * b
        return resultado
    except TypeError:
        return "Error: Tipo de dato no válido"

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("No es posible dividir entre cero")
        resultado = a / b
        return resultado
    except (ZeroDivisionError, TypeError) as e:
        return f"Error: {str(e)}"
import operaciones

# Ejemplo de uso
a = 10
b = 2

# Realizar operaciones
resultado_suma = operaciones.suma(a, b)
resultado_resta = operaciones.resta(a, b)
resultado_producto = operaciones.producto(a, b)
resultado_division = operaciones.division(a, b)

# Mostrar resultados
print(f"Suma: {resultado_suma}")
print(f"Resta: {resultado_resta}")
print(f"Producto: {resultado_producto}")
print(f"División: {resultado_division}")
