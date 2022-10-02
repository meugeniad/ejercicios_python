#v1 - Funciones con tareas específicas

def es_un_numero (numero):
    for digito in numero:
        if digito not in '0123456789':
            return False
    
    return True

def es_bisiesto (numero):
    
    if numero%4 != 0:
        return 'no es bisiesto'
    elif numero%4 == 0 and numero%100 != 0:
        return 'es bisiesto'
    elif numero%4 == 0 and numero%100 == 0 and numero%400 == 0:
        return 'es bisiesto'
    else:
        return 'no es bisiesto'
    
numero = input('Ingresame un año: ')
valida = es_un_numero(numero)

if valida :  
    print(f'El año {numero} {es_bisiesto(int(numero))} ')
else:
    print('Debe ingresar un numero.')
    
#v2 . Una sola función

def es_bisiesto (numero):
    for digito in numero:
        if digito not in '0123456789':
            return "Debe ingresar un número"
    
    anio = int(numero)
    
    if anio%4 != 0:
        return (f'El año {numero} no es bisiesto')
    elif anio%4 == 0 and anio%100 != 0:
        return (f'El año {numero} es bisiesto')
    elif anio%4 == 0 and anio%100 == 0 and anio%400 == 0:
        return (f'El año {numero} es bisiesto')
    else:
        return (f'El año {numero} no es bisiesto')
    
numero = input('Ingresame un año: ')

print(es_bisiesto(numero))