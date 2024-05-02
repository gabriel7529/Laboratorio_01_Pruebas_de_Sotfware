
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
# clasificacion = clasificar_triangulo(3, 3, 3)
# print(f"El triángulo es: {clasificacion}") 

# Caso de Prueba 2 
#TODO: Este caso funciona por el tema de que lo ingresamos directamente y no por el input
# clasificacion = clasificar_triangulo(5.3, 6, 7.2)
# print(f"El triángulo es: {clasificacion}") 

# #Caso de Prueba 3
# clasificacion = clasificar_triangulo(-5, -6, -7)
# print(f"El triángulo es: {clasificacion}") 

# Caso de Prueba 4
# clasificacion = clasificar_triangulo(5, 6, 5)
# print(f"El triángulo es: {clasificacion}") 

# Caso de Prueba 5
# clasificacion = clasificar_triangulo(5, 5, 10)
# print(f"El triángulo es: {clasificacion}") 

# Caso de Prueba 6
# clasificacion = clasificar_triangulo(0, 0, 0)
# print(f"El triángulo es: {clasificacion}") 

# Caso de Prueba 7
# clasificacion = clasificar_triangulo(True, "3.5", 2.6)
# print(f"El triángulo es: {clasificacion}") 

# Caso de Prueba 8
lado1 = int(input("Ingrese la longitud del primer lado: ")) 
lado2 = int(input("Ingrese la longitud del segundo lado: ")) 
lado3 = int(input("Ingrese la longitud del tercer lado: "))  
clasificacion = clasificar_triangulo(lado1, lado2, lado3)
print(f"El triángulo es: {clasificacion}") 