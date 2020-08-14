print("Calculadora")
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
opc = int(input ("""Qué desea hacer:
 1. Sumar
 2. Restar
 3. Multiplicar
 4. Dividir
 """))

if opc == 1:
    suma = n1 + n2
    print (suma)
elif opc == 2:
    resta = n1 - n2
    print (resta)
elif opc == 3:
    mult = n1 * n2
    print (mult)
elif opc == 4:
    if not n2 == 0:
        div = n1 / n2
        print (div)
    else:
        print ("Division por 0 no determinada")