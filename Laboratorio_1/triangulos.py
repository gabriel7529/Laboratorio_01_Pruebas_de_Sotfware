
def clasificar_triangulo(lado1, lado2, lado3):   
    """   Esta función clasifica un triángulo según sus lados.    
    Args:       
          lado1: La longitud del primer lado.       
          lado2: La longitud del segundo lado.       
          lado3: La longitud del tercer lado.    
    Returns:       
        Un string que indica si el triángulo es escaleno, isósceles, equilátero o inválido.   
        """    
    # Verificar si el triángulo es válido   
    if lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:     
        return "Triángulo inválido"    
    

    if lado1 == lado2 == lado3:     
        return "Triángulo equilátero"   
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:     
        return "Triángulo isósceles"   
    else:     
        return "Triángulo escaleno"  
    # Clasificar el triángulo y mostrar el resultado 

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
#Verificar que la función determine el triangulo con datos decimales, boolean y String
#Respuesta Esperada:  Triángulo inválido

#Código
# clasificacion = clasificar_triangulo(True, "3.5", 2.6)
# print(f"El triángulo es: {clasificacion}") 

# Caso de Prueba 8
#Verificar que la función determine el triangulo con el ingreso de datos por el usuario en una misma linea.
#Respuesta Esperada: Triángulo inválido

#Código
# lado1 = int(input("Ingrese la longitud del primer lado: ")) 
# lado2 = int(input("Ingrese la longitud del segundo lado: ")) 
# lado3 = int(input("Ingrese la longitud del tercer lado: "))  
# clasificacion = clasificar_triangulo(lado1, lado2, lado3)
# print(f"El triángulo es: {clasificacion}") 

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


