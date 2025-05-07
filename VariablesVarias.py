 # primer ejercicio
def suma_numeros_pares_positivos():
    suma = 0    # la suma tiene que empezar en 0
    for i in range(5):   # aca se repite un rango de 5 para pedir los 5 numeros 
        numero = int(input("Ingrese un número: "))
        if numero > 0 and numero % 2 == 0:   # aca determina si el numero es positivo y par
            suma += numero
    print(f"La suma de los positivos y pares es: {suma}")   # sale el resultado de la suma 
# segundo ejercicio 
def pasos_de_la_vida():
    edad = int(input("Ingrese su edad."))
    if edad > 0: # la edad debe ser mayor a 0 
        if edad < 13:   
            print ("eres niño.")
        elif edad >= 13 and edad <= 17:      # con el if, elif, y else, se hacen los cortes, para determinar la edad 
            print ("eres adolecente.")
        elif edad > 17 and edad < 60:
         print ("eres adulto.") 
        else:
            print ("eres adulto mayor.")
    else:
        print ("No puede ser un numero negativo negativo.")

 # tercer ejecicio
def contador_vocales():
    # inicializamos los contadores con 0 
    a = 0
    e = 0 
    i = 0
    o = 0
    u = 0

    palabra = input("Ingrese una palabra: ")

    for letra in palabra:
        letra = letra.lower() # aca se convierte la palabra en minuscula para que no afecte el conteo
        if letra == 'a':    # si tiene la letra a suma un a al contador
            a += 1
        elif letra == 'e':
            e += 1
        elif letra == 'i':   # y asi susecibamente con todas las vocales
            i += 1
        elif letra == 'o':
            o += 1
        elif letra == 'u':
            u += 1

    print("La palabra tiene:")  # y aca muestra cuantas veces aparecio la vocal en la palabra 
    print(f"a: {a}")
    print(f"e: {e}")
    print(f"i: {i}")
    print(f"o: {o}")
    print(f"u: {u}")

# es un menu para que quede mas ordenado

while True:
    print ("______________________________")
    print("1) suma de numeros pares positivos.")
    print("2) pasos de la vida.")
    print("3) Contador de vocales.")
    print("4) Salir.")

    opcion = input("elija el numero de la opcion que desea. ")

    if opcion == '1':
        suma_numeros_pares_positivos()
    elif opcion == '2':
        pasos_de_la_vida()
    elif opcion == '3':
        contador_vocales()
    elif opcion == '4':
        print("fin.")
    
