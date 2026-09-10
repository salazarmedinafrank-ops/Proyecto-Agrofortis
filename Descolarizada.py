num1, num2, num3 = map(int, input("Ingrese 3 números enteros separados por espacios: ").split())

if num1 == num2 and num2 == num3:
    print("Los tres números son iguales")
else:
    if num1 == num2:
        print("El número 1 y el número 2 son iguales")
    else:
        if num1 == num3:
            print("El número 1 y el número 3 son iguales")
        else:
            if num2 == num3:
                print("El número 2 y el número 3 son iguales")
            else:
                print("No hay números iguales")

print("Número 1:", num1)
print("Número 2:", num2)
print("Número 3:", num3)
if num1 > 0:
    print("El número", num1, "es positivo")
else:
    if num1 < 0:
        print("El número", num1, "es negativo")

if num2 > 0:
    print("El número", num2, "es positivo")
else:
    if num2 < 0:
        print("El número", num2, "es negativo")

if num3 > 0:
    print("El número", num3, "es positivo")
else:
    if num3 < 0:
        print("El número", num3, "es negativo")


