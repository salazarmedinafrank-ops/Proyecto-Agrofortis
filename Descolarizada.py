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
        
# Buscar el mayor
if num1 > num2:
    mayor = num1
else:
    mayor = num2

if mayor > num3:
    mayor = mayor
else:
    mayor = num3

# Buscar el menor
if num1 < num2:
    menor = num1
else:
    menor = num2

if menor < num3:
    menor = menor
else:
    menor = num3

# Buscar el intermedio
if num1 > num2:
    if num2 > num3:
        intermedio = num2
    else:
        if num1 < num3:
            intermedio = num1
        else:
            intermedio = num3
else:
    if num1 > num3:
        intermedio = num1
    else:
        if num2 < num3:
            intermedio = num2
        else:
            intermedio = num3

print("El mayor es:", mayor)
print("El menor es:", menor)
print("El numero intermedio es:", intermedio)


