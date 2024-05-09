# Caso de Prueba 18 ------------------------------
def contiene_operadores(valor):
    operadores = ['+', '-', '*', '/']
    return any(op in valor for op in operadores)
# -------------------------------------------------

def clasificar_triangulo(lado1, lado2, lado3):
    # Caso de prueba 16 ---------------------------
    # Verificar si los lados son enteros literales
    try:
        lado1 = int(lado1)
        lado2 = int(lado2)
        lado3 = int(lado3)
    except ValueError:
        return "El triángulo debe contener sólo valores enteros y en formato literal"
    # ---------------------------------------------------------------------------------

    # Caso de prueba 17    
    try:
        lado1 = int(lado1)
        lado2 = int(lado2)
        lado3 = int(lado3)
    except ValueError:
        return  "El triángulo debe contener sólo valores enteros,no ingrese valores en numeros romanos"
    # ---------------------------------------------------------------------------------

    if not lado1 or not lado2 or not lado3:
        return("Triángulo inválido, Ingrese los datos correctamente")
  
    # Caso de Prueba 18
    # Verificar si los lados contienen operadores
    if contiene_operadores(lado1) or contiene_operadores(lado2) or contiene_operadores(lado3):
        return "Los lados no deben contener operadores"
    # ---------------------------------------------------------------------------------

    # Verificar si el triángulo es válido
    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        return "Triángulo inválido"

    # Clasificar el triángulo
    if lado1 == lado2 == lado3:
        return "Triángulo equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Triángulo isósceles"
    else:
        return "Triángulo escaleno"

# Solicitar al usuario la longitud de los lados y verificar si son enteros literales
lado1 = input("Ingrese la longitud del primer lado: ")
lado2 = input("Ingrese la longitud del segundo lado: ")
lado3 = input("Ingrese la longitud del tercer lado: ")

clasificacion = clasificar_triangulo(lado1, lado2, lado3) 
print(f"El triángulo es: {clasificacion}") 

