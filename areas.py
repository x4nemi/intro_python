def areaCuadrado():
    lado = float(input("Cuadrado\nMedida del lado: "))
    area = lado ** 2
    print(f"El área del cuadrado es {area}\n")

def areaTriangulo():
    altura = float(input("Triángulo\nMedida de la altura: "))
    base = float(input("Medida de la base: "))
    area = altura * base / 2
    print(f"El área del triangulo es {area}\n")

def areaCirculo():
    radio = float(input("Círculo\nMedida del radio: "))
    area = 3.14159 * radio ** 2
    print(f"El área del círculo es {area}\n")

def menu():
    while(True):
        print("1) Area Cuadrado")
        print("2) Area Triángulo")
        print("3) Area Circulo")
        print("0) Salir")
        opcion = int(input("Opcion: "))

        if opcion == 0:
            break
        if opcion == 1:
            areaCuadrado()
        elif opcion == 2:
            areaTriangulo()
        elif opcion == 3:
            areaCirculo()
        else:
            print("Opcion incorrecta\n")

menu()