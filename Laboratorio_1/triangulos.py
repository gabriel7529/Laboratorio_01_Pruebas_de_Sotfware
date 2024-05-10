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
# lado1 = input("Ingrese la longitud del primer lado: ")
# lado2 = input("Ingrese la longitud del segundo lado: ")
# lado3 = input("Ingrese la longitud del tercer lado: ")

# clasificacion = clasificar_triangulo(lado1, lado2, lado3) 
# print(f"El triángulo es: {clasificacion}") 


#lado1 = int(input("Ingrese la longitud del primer lado: ")) 
#lado2 = int(input("Ingrese la longitud del segundo lado: ")) 
#lado3 = int(input("Ingrese la longitud del tercer lado: "))  
# Clasificar el triángulo y mostrar el resultado


#Caso de Prueba 1
#Verificar si la función determina si el triangulo es equilatero

#Código
# clasificacion = clasificar_triangulo(3, 3, 3)
# Respuesta Esperada: Triángulo equilátero
# print(f"El triángulo es: {clasificacion}") 

# Caso de Prueba 2 
#TODO: Este caso funciona por el tema de que lo ingresamos directamente y no por el input
#Verificar que el función determine que tipo de triangulo es con datos decimales

#Código
# clasificacion = clasificar_triangulo(5.3, 6.8, 7.2)
# Respuesta Esperada: Triángulo escaleno
# print(f"El triángulo es: {clasificacion}") 

# #Caso de Prueba 3
#Verificar que la función determine el triangulo con datos negativos
#Respuesta Esperada: 
#Triángulo inválido
#Triángulo inválido
#Triángulo inválido

#Código
# clasificacion = clasificar_triangulo(-5, -6, -7)
# print(f"El triángulo es: {clasificacion}") 
# clasificacion = clasificar_triangulo(5, -6, 7)
# print(f"El triángulo es: {clasificacion}") 
# clasificacion = clasificar_triangulo(5, -6, -7)
# print(f"El triángulo es: {clasificacion}") 

# Caso de Prueba 4
#Verificar que la función determine el triangulo con datos enteros
#Respuesta Esperada: Triángulo isósceles

#Código
# clasificacion = clasificar_triangulo(5, 6, 5)
# print(f"El triángulo es: {clasificacion}") 

# Caso de Prueba 5
#Verificar que la función determine el triangulo donde la suma de dos lados da el valor del tercer lado
#Respuesta Esperada: Triángulo inválido

#Código
# clasificacion = clasificar_triangulo(5, 5, 10)
# print(f"El triángulo es: {clasificacion}") 

# Caso de Prueba 6
#Verificar que la función determine el triangulo con datos iguales a 0
#Respuesta Esperada: Triángulo inválido

#Código
# clasificacion = clasificar_triangulo(0, 0, 0)
# print(f"El triángulo es: {clasificacion}") 

# Caso de Prueba 7
# Verificar que la función determine el triangulo con datos decimales, boolean y String
# Respuesta Esperada:  Triángulo inválido

# Código
# clasificacion = clasificar_triangulo(True, "3.5", 2.6)
# print(f"El triángulo es: {clasificacion}") 

# Caso de Prueba 8
#Verificar que la función determine el triangulo con el ingreso de datos por el usuario en una misma linea.
#Respuesta Esperada: Triángulo inválido

#Código
lado1 = input("Ingrese la longitud del primer lado: ")
lado2 = input("Ingrese la longitud del segundo lado: ") 
lado3 = input("Ingrese la longitud del tercer lado: ")  
clasificacion = clasificar_triangulo(lado1, lado2, lado3)
print(f"El triángulo es: {clasificacion}") 

##Pruebas del Libro 
#Caso de prueba 9
#Verificar que la función determine el triangulo escaleno
#Respuesta Esperada: Triángulo escaleno

#Código
# clasificacion = clasificar_triangulo(2, 8, 7)
# print(f"El triángulo es: {clasificacion}")

#Caso de Prueba 10
#Verificar que la función determine el triangulo isósceles con datos y sus permutaciones
#Respuesta Esperada: 
#Triángulo isósceles
#Triángulo isósceles
#Triángulo isósceles

#Código
# clasificacion = clasificar_triangulo(5, 5, 7)
# print(f"El triángulo es: {clasificacion}")
# clasificacion = clasificar_triangulo(7, 5, 5)
# print(f"El triángulo es: {clasificacion}")
# clasificacion = clasificar_triangulo(5, 7, 5)
# print(f"El triángulo es: {clasificacion}")


#Caso de Prueba 11
#Verificar que la función determine el triangulo con datos con el comportamiento de la 
# Prueba 6 y sus permutaciones
#Respuesta Esperada:
#Triángulo inválido
#Triángulo inválido
#Triángulo inválido

#Código
# clasificacion = clasificar_triangulo(5, 6, 11)
# print(f"El triángulo es: {clasificacion}")
# clasificacion = clasificar_triangulo(6, 11, 5)
# print(f"El triángulo es: {clasificacion}")
# clasificacion = clasificar_triangulo(11, 6, 5)
# print(f"El triángulo es: {clasificacion}")

#Caso de Prueba 12
#Verificar que la función determine el triangulo con datos donde la suma de sus dos lados son menores que el tercero.
#Respuesta Esperada:
#Triángulo inválido
#Triángulo inválido
#Triángulo inválido

#Código
# clasificacion = clasificar_triangulo(4, 5, 11)
# print(f"El triángulo es: {clasificacion}")
# clasificacion = clasificar_triangulo(12, 2, 3)
# print(f"El triángulo es: {clasificacion}")
# clasificacion = clasificar_triangulo(1, 15, 2)
# print(f"El triángulo es: {clasificacion}")

#Caso de Prueba 13
#Verificar que la función determine el triangulo si el usuario se olvida de poner un valor
#Respuesta Esperada:
#Triángulo inválido

#Código
# lado1 = int(input("Ingrese la longitud del primer lado: ")) 
# lado2 = int(input("Ingrese la longitud del segundo lado: ")) 
# lado3 = int(input("Ingrese la longitud del tercer lado: "))  
# clasificacion = clasificar_triangulo(lado1, lado2, lado3)
# print(f"El triángulo es: {clasificacion}") 


#  Casos de Prueba Adicionales ////////////
#Caso de prueba 14
# Entrada de valores con espacios adicionales
# El programa debe clasificar el triangulo aunque 
# existan espacios al inicio o al final de cada valor ingresado
#Respuesta Esperada:
# Clasificacion correcta del triangulo ingresado

# Caso de prueba 15
# Entrada de valores muy grandes
# El programa debe clasificar el triangulo aunque 
# se ingresen valores muy grandes
#Codigo:
# clasificacion = clasificar_triangulo(999999999, 999999999, 999999999)
# print(f"El triángulo es: {clasificacion}") 
#Respuesta Esperada:
# Triangulo Equilatero

#Caso de prueba 16
# Entrada de valores muy grandes y con formato cientiefico "e"
#Codigo:
#clasificacion = clasificar_triangulo(1e10, 2e10, 2e10)
#print(f"El triángulo es: {clasificacion}") 
#Respuesta Esperada:
# Triangulo Isosceles

#Caso de prueba 17
# Entrada de valores en formato de Numeros Romanos 
#Respuesta Esperada:
# Error por la función int(input()) 
# no puede convertir números romanos en números enteros.

# Caso de prueba 18
# Entrada de valores como operaciones matematicas
# Codigo
#clasificacion = clasificar_triangulo(2+4, 3*2, 1*6) 
# Respuesta esperada
# Error de conversion, la funcion int(input()) no realiza operaciones 

