def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: División por cero"
    return x / y

def calculadora():
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    while True:
        seleccion = input("Ingrese el número de la operación (1/2/3/4): ")

        if seleccion in ('1', '2', '3', '4'):
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if seleccion == '1':
                print(f"{num1} + {num2} = {suma(num1, num2)}")
            elif seleccion == '2':
                print(f"{num1} - {num2} = {resta(num1, num2)}")
            elif seleccion == '3':
                print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
            elif seleccion == '4':
                print(f"{num1} / {num2} = {division(num1, num2)}")
        
        else:
            print("Selección no válida")

        # Preguntar si desea realizar otra operación
        otra_operacion = input("¿Desea realizar otra operación? (sí/no): ")
        if otra_operacion.lower() != 'sí':
            break

if __name__ == "__main__":
    calculadora()
