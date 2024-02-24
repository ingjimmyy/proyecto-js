
numero1= int(input("Ingresa el primer valor: "))
numero2= int(input("ingresa el segundo valor: "))
eleccion= 0

while eleccion !=6:
    print("""
    indique la operacion a realizar:
    1)suma
    2)resta
    3)multiplicacion
    4)divicion
    5)cambio de valores
    6)salir
    """)
    eleccion=int(input())

    if eleccion == 1:
        print(" ")
        print("Resultado: ", numero1, "+", numero2, "=", numero1+numero2)

    if eleccion ==2:
        print(" ")
        print("Resultado: ", numero1, "-", numero2, "=", numero1-numero2)

    if eleccion ==3:
        print(" ")
        print("Resultado: ", numero1, "*", numero2, "=", numero1*numero2)

    if eleccion ==4:
        print(" ")
        print("Resultado: ", numero1, "/", numero2, "=", numero1/numero2)

    if eleccion ==5:
        numero1= int(input("Ingresa el primer valor: "))
        numero2= int(input("ingresa el segundo valor: "))

    if eleccion ==6:
        print("GRACIAS POR USAR LA CALCULADORA HECHA POR JIMMY CRACK")