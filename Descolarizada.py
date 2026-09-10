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

