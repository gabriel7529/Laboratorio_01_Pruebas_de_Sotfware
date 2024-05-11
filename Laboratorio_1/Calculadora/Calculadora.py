#!/usr/bin/python
import os

# FUNCIONES DE LA CALCULADORA

# FUNCION QUE SUMA DOS VALORES
def sumar(valor1=0, valor2=0):
    return valor1 + valor2

# FUNCION QUE RESTA DOS VALORES
def restar(valor1=0, valor2=0):
    return valor1 - valor2

# FUNCION QUE MULTIPLICA DOS VALORES
def multiplicar(valor1=0, valor2=0):
    return valor1 * valor2


# FUNCION QUE DIVIDE DOS VALORES
def dividir(valor1=0, valor2=0):
    if valor2 == 0:
        print("No se puede dividir entre 0")
        return 0
    return valor1 / valor2


# FUNCIONES DE LA CALCULADORA
def menu():
    # MENU DE OPCIONES
    print("** ::::::::::::::::::::::::: **")
    print(":: Seleccione una operación ::")
    print("** ::::::::::::::::::::::::: **")
    print("-------------------------------")
    print("| Suma:             ->  1     |")
    print("| Resta:            ->  2     |")
    print("| Multiplicación:   ->  3     |")
    print("| División:         ->  4     |")
    print("| Salir:            ->  s     |")
    print("-------------------------------")
    print("** ::::::::::::::::::::::::: **")
    print("\n")
    # MENU DE OPCIONES

def opciones():
    opcion = input("Seleccione una Opción... ")
    return opcion

#Realizando pruebas para el caso de prueba 11

def valores():
   
    try:
        #Modificaciones para caso de prueba 11 
        valor1 = input("Ingrese su primer valor: ")
        valor2 = input("Ingrese su segundo valor: ")
        if 'e' in valor1 or 'e' in valor2:
            print("Por favor, no ingrese valores en formato de notación científica.")
            return None, None
        valor1 = float(valor1)
        valor2 = float(valor2)
        #------------------------------------------
    except ValueError:
        print("Operación no realizada, error al ingresar los valores. Intente nuevamente.")
        return None, None
    return valor1, valor2

def errorOperacion():
    regresar = input("¿Quiere realizar una nueva operación [S/N]? ")
    return regresar


while True:
    menuPrincipal = menu()
    opc = opciones()

    if opc == 's':
        print("Saliendo...")
        break
    elif opc == '1':
        print("\n")
        print("** Entrando al módulo de Suma **")
        valor1, valor2 = valores()
        if(valor1 != None or valor2 != None):
             resultadoSuma = sumar(valor1, valor2)
             print("El resultado de su suma es: " + str(resultadoSuma))
        nuevaOperacion = errorOperacion()
    elif opc == '2':
        print("\n")
        print("** Entrando al módulo de Resta **")
        valor1, valor2 = valores()
        if(valor1 != None or valor2 != None):
             resultadoResta = restar(valor1, valor2)
             print("El resultado de su resta es: " + str(resultadoResta))
        nuevaOperacion = errorOperacion()
    elif opc == '3':
        print("\n")
        print("** Entrando al módulo de Multiplicación **")
        valor1, valor2 = valores()
        #Modificacion para caso de prueba 11
        if(valor1 != None or valor2 != None):
            resultadoMultiplicacion = multiplicar(valor1, valor2)
            print("El resultado de su Multiplicación es: " + str(resultadoMultiplicacion))
        nuevaOperacion = errorOperacion()
   
    elif opc == '4':
        print("\n")
        print("** Entrando al módulo de División **")
        valor1, valor2 = valores()
        resultadoDivision = dividir(valor1, valor2)
        print("El resultado de su División es: " + str(resultadoDivision))
        nuevaOperacion = errorOperacion()
    else:
        print("Opción no válida")
        continue

    if nuevaOperacion.upper() != "S" :
        print("Saliendo...")
        break

        
