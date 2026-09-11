print("CALCULADORA DE AREAS")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

continuar = "s"

while continuar == "s":

    print("\n========== MENU ==========")
    print("1. Calcular área")
    print("2. Salir")

    menu = input("Ingrese una opción: ")

    if menu == "1":

        print("\nSeleccione la figura:")
        print("1. Cuadrado")
        print("2. Círculo")
        print("3. Rectángulo")
        print("4. Triángulo")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":

            lado = input("Ingrese el lado del cuadrado: ")

            if lado.isdigit():
                lado = float(lado)
                area = lado * lado
                print("El área del cuadrado es:", area)
            else:
                print("Error: solo se permiten números.")

        elif opcion == "2":

            radio = input("Ingrese el radio del círculo: ")

            try:
                radio = float(radio)
                area = 3.1416 * radio ** 2
                print("El área del círculo es:", area)
            except:
                print("Error: solo se permiten números.")

        elif opcion == "3":

            base = input("Ingrese la base del rectángulo: ")
            altura = input("Ingrese la altura del rectángulo: ")

            try:
                base = float(base)
                altura = float(altura)
                area = base * altura
                print("El área del rectángulo es:", area)
            except:
                print("Error: solo se permiten números.")

        elif opcion == "4":

            base = input("Ingrese la base del triángulo: ")
            altura = input("Ingrese la altura del triángulo: ")

            try:
                base = float(base)
                altura = float(altura)
                area = (base * altura) / 2
                print("El área del triángulo es:", area)
            except:
                print("Error: solo se permiten números.")

        else:
            print("Error: opción no válida.")

    elif menu == "2":

        continuar = "n"
        print("\nPrograma finalizado.")

    else:
        print("Error: opción no válida.")

print("Usuario:", nombre, apellido)