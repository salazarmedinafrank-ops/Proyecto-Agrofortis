num1, num2, num3 = map(int, input("Ingrese 3 numeros: ").split())
print("positivos y negativos")

if num1 > 0:
    print(num1, "es positivo")
elif num1 < 0:
    print(num1, "es negativo")

if num2 > 0:
    print(num2, "es positivo")
elif num2 < 0:
    print(num2, "es negativo")

if num3 > 0:
    print(num3, "es positivo")
elif num3 < 0:
    print(num3, "es negativo")

# Buscar el mayor
if num1 >= num2 and num1 >= num3: 
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

# Buscar el menor
if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

# Buscar el intermedio
if num1 > num2 and num1 < num3:
    Intermedio = num1
elif num2 > num1 and num2 < num3:
    Intermedio = num2
else: 
    Intermedio = num3

print("El mayor es:", mayor)
print("El menor es:", menor)
print("El numero intermedio es:",Intermedio)