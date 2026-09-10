num1, num2, num3 = map(int, input("Ingrese 3 numeros: ").split())

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