#Ejercicio 1
# repetir = True
# while repetir:
#     print('''
# =================
#     Opciones
# =================
# 1. Suma de dos números
# 2. Resta de dos números (primero - segundo)
# 3. Multiplicación de dos números
# 4. Finalizar
# ''')
#     opcion_menu = int(input("\nIngrese la operación a realizar: "))
      
#     if opcion_menu < 4:
#         numero1 = int(input("\nIngrese el primer número para operar: "))
#         numero2 = int(input("Ingrese el segundo número para operar: "))
    
#     if opcion_menu == 1:
#         suma = numero1 + numero2
#         print("\nLa suma de los números es ", suma )
#     elif opcion_menu == 2:
#         diferencia = numero1 - numero2
#         print("\nLa diferencia entre primero y el segundo es: ", diferencia)
#     elif opcion_menu == 3:
#         multiplicacion = numero1 * numero2
#         print("\nLa multiplicación de los dos nuemeros es: ", multiplicacion)
#     elif opcion_menu == 4:
#         print( "\nSe finaliza el programa")
#         repetir = False
#     else:
#         print("\nLa opción del menú no es correcta")
    
#Ejercicio 2

# repetir = True
# while repetir:
#     numero = int(input("\nIngrese un número impar: "))
#     if numero%2 == 0:
#         print("\nEl número no es impar. Vuelva a intentarlo")
#     else:
#         print("\nEl dato es correcto. El programa finalizará")  
#         repetir = False      
        
#Ejercicio 3
# #Modalidad 1
# suma = 0
# for numero in range (1,100,2):
#     suma = suma + numero
# print("La suma de los impares de 0 a 100 es: ",suma)
# #Modalidad 2
# suma2 = sum(range(1,100,2))
# print("La suma de los impares de 0 a 100 es: ",suma2)


#Ejercicio 4
# print("\nSe calculará la media aritmética para los valores que introduzca")
# suma = 0
# cantidad = int(input("¿Cuántos números desea introducir? "))
# if cantidad != 0:
#     for indice in range (1, cantidad+1):
#         numero = int(input("\nIngrese un número: "))
#         suma = suma + numero
#     media_aritmetica = suma / cantidad
#     print("\nLa media aritmética calculada es: ", media_aritmetica)
# else:
#     print("\nEl 0 no es valido para esta operación. El programa no se ejecutará")

#Ejericio 5
lista = [0,1,2,3,4,5,6,7,8,9]
numeros = [1, 3, 6, 9]
repetir = True
while repetir:
    numero = int(input("\nIngrese un valor entre 0 y 9: "))
    if numero in lista:
        if numero in numeros:
            print("\nEl número ingresado esta en la lista predefinida")
        else: 
            print("\nEl número ingresado no esta en la lista predefinida")
        repetir = False
    else:   
        print("\nEl número ingresado no es válido. Vuelva a intentarlo")

#Ejericio 6
# lista1 = list(range(0,11,1))
# print("Lista 1:", lista1)
# lista2 = list(range(-10,1,1))
# print("\nLista 2:" ,lista2)
# lista3 = list(range(0,21,2))
# print("\nLista 3:" ,lista3)
# lista4 = list(range(-19,0,2))
# print("\nLista 4:" ,lista4)
# lista5 = list(range(0,51,5))
# print("\nLista 5:" ,lista5)

#Ejercicio 7
# lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
# lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
# lista_3 = []
# for valor in lista_1:
#     if valor in lista_2 and valor not in lista_3:
#         lista_3 = lista_3 + [valor]
# print("La lista generada es", lista_3)
    
    
    