#EJERCICIO NUMERO 1 DE PC3
while True:
    try:
        # Solicitar al usuario una fracción en formato X/Y
        fraccion = input("Ingrese una fracción en formato X/Y (X e Y deben ser enteros, X >= Y, Y != 0): ")
        
        # Separar la fracción en los valores X e Y
        x, y = map(int, fraccion.split('/'))
        
        # Verificar las condiciones de X e Y
        if x < 0 or y <= 0:
            raise ValueError("X e Y deben ser enteros positivos, Y no puede ser igual a 0")
        if x < y:
            raise ValueError("X debe ser mayor o igual a Y")
        
        # Calcular el porcentaje
        porcentaje = (x / y) * 100
        
        # Redondear al número entero más cercano
        porcentaje_redondeado = round(porcentaje)
        
        # Determinar el resultado según las condiciones dadas
        if porcentaje_redondeado < 1:
            resultado = "E"
        elif porcentaje_redondeado > 99:
            resultado = "F"
        else:
            resultado = f"{porcentaje_redondeado}%"
        
        # Mostrar el resultado
        print(f"La cantidad de combustible en el tanque es: {resultado}")
        
        # Salir del bucle
        break
    
    except ValueError as e:
        print(f"Error: {e}. Por favor, ingrese una fracción válida.")
    
    except ZeroDivisionError:
        print("Error: Y no puede ser igual a 0. Por favor, ingrese una fracción válida.")
