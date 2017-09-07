while True:
    print("opciones")
    print("introduce 'suma' para sumar dos numeros")
    print("introduce 'resta' para restar dos numeros")
    print("introduce 'multiplicacion' para multiplicar dos numeros")
    print("introduce 'division' para dividir dos numeros")
    print("introduce 'salir' para salir del programa")
    user_input = (eval(input("")))

    if user_input == "salir":
        break

    elif user_input == "suma":
        num1 = float(eval(input("Introduce un numero: ")))
        num2 = float(eval(input("Introduce otro numero: ")))
        result = str((num1 + num2))
        print(("la respuesta es " + result))

    elif user_input == "resta":
        num1 = float(eval(input("Introduce un numero: ")))
        num2 = float(eval(input("Introduce otro numero: ")))
        result = str((num1 - num2))
        print(("la respuesta es " + result))

    elif user_input == "multiplicacion":
        num1 = float(eval(input("Introduce un numero: ")))
        num2 = float(eval(input("Introduce otro numero: ")))
        result = str((num1 * num2))
        print(("la respuesta es " + result))

    elif user_input == "dividision":
        num1 = float(eval(input("Introduce un numero: ")))
        num2 = float(eval(input("Introduce otro numero: ")))
        result = str((num1 / num2))
        print(("la respuesta es " + result))

    else:
        print(("entrada inncorecta"))