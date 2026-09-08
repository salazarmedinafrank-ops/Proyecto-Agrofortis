num1, num2, num3 = map(int, input("Ingrese 3 numeros: ").split())

if num1 == num2 and num2 == num3:
    print("Los tres numeros son iguales")
elif num1 >= num2 and num1 >= num3:
    print("El mayor es:", num1)
elif num2 >= num1 and num2 >= num3:
    print("El mayor es:", num2)
else:
    print("El mayor es:", num3)













