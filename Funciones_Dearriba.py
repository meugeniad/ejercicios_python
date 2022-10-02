#Ejericio 1 area de un rectángulo
# def es_un_numero (numero):
#     for digito in numero:
#         if digito not in '0123456789':
#             return False
    
#     return True

# def area_rectangulo (base, altura):
#     if not es_un_numero(base):
#        return  print('Debe ingresar un numero para la base.') 
#     if not es_un_numero(altura):
#         return  print('Debe ingresar un numero para la altura.')

#     return print(f'El área del rectángulo es {int(base)*int(altura)} ')

# base = input('Ingresame la base de su rectángulo: ')
# altura = input('Ingresame la altura de su rectángulo: ')

# area_rectangulo(base, altura)  


#Ejercicio 2 area de un círuclo

# def es_un_numero (numero):
#     for digito in numero:
#         if digito not in '0123456789':
#             return False
    
#     return True

# def area_ciruclo (radio):
#     import math

#     if not es_un_numero(radio):
#        return  print('Debe ingresar un número para el radio de su círculo.') 
   
#     return print(f'El área de su círuclo es {math.pi*int(radio)**2} ')

# radio = input('Ingresa el radio de tu círculo: ')

# area_ciruclo(radio)  

#Ejercicio 3 compara dos números

# def relacion (param1, param2):
#     if param1 > param2:
#        return 1
#     elif param1 < param2:
#        return -1
#     else:
#         return 0
    

# numero1 = int(input('Ingre el primer número a comparar: '))
# numero2 = int(input('Ingre el segundo número a comparar: '))

# print (f"El resultado de la comparación es {relacion (numero1, numero2)}")

#Ejercicio 4 número intermedio

# def intermedio(*args):
#     return sum(args)/2

# print(f'El valor intermedio es {intermedio(-12,24)}') 


#Ejercicio 5 recortar()

# def recortar(num, lim_inf, lim_sup):
#     if num < lim_inf:
#         return lim_inf
#     elif num > lim_sup:
#         return lim_sup
#     else:
#         return num
    
# print(recortar(15, 0, 10))

#Ejercicio 6 separar en dos listas, pares e impares
# lista = [1, 15, 0, 13, 15, 10, 13, 18,1]
# a=[]
# b=[]
# contador=0
# for element in lista:
#     if contador % 2 == 0:
#         a.append(element)
#     else:
#         b.append(element)
#     contador+=1
    
    
# print(a.sort(),b.sort())

def es_un_numero (numero):
    for digito in numero:
        if digito not in '0123456789':
            return False
    return True

def separar(lista):
    par=[]
    impar=[]
    for elemento in lista:
        if elemento% 2 == 0:
            par.append(elemento)
        else:
            impar.append(elemento)
    par.sort()
    impar.sort()
    return par, impar

cantidad = int(input("Ingrese la cantidad de números para la lista: "))
  
lista = []
contador = 0

while contador < cantidad:
  numero = input("Agregue un número en la lista: ")
  if es_un_numero(numero):
    lista.append(int(numero))
    contador +=1
  else:
      print("El dato es incorrecto. Sólo se aceptan número\n")
      
pares, impares = separar(lista)
 
print (f"La lista de pares ordenados: {pares}")
print (f"La lista de impares ordenados: {impares}")

# def separar(*arg):
#     par=[]
#     impar=[]
#     for elemento in arg[:]:
#         if elemento% 2 == 0:
#             par.append(elemento)
#         else:
#             impar.append(elemento)
#     par.sort()
#     impar.sort()
#     return par, impar

      
# pares, impares = separar(6,5,2,1,7)
 
# print (f"La lista de pares ordenados: {pares}")
# print (f"La lista de impares ordenados: {impares}")
       
       

   

