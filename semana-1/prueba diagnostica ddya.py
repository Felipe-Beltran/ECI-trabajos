def main():
    a = int(input("Ingrese un numero: "))
    
    if a % 2 == 0:
        print("Es un numero par")
    else:
        print("Es un numero impar")
        
    if a == 0:
        print("Es cero el numero")

    b = 2
    numero1 = 1
    numero2 = 1
    numerototal = 0

    vector = [1 for i in range(100)]
    
    while b < 100:
        numerototal = numero1 + numero2
        vector[b] = numerototal
        numero1 = numero2
        numero2 = numerototal
        b = b + 1
        
    fibo1 = 0
    b = 0
    while b < 100:
        if vector[b] == a:
            print("El primer numero es de Fibonacci")
            fibo1 = 1
        b = b + 1
            
    dos1 = 0
    c = 1
    while c <= abs(a):
        if a != 0 and a % c == 0:
            dos1 = dos1 + 1
        c = c + 1

    primo1 = 0
    if dos1 == 2:
        print("El primer numero es primo")
        primo1 = 1
    else:
        print("El primer numero NO es primo")

    nuevo = int(input("\nIngrese un segundo numero (debe ser primo y Fibonacci): "))
    
    fibo2 = 0
    b = 0
    while b < 100:
        if vector[b] == nuevo:
            fibo2 = 1
        b = b + 1

    dos2 = 0
    c = 1
    while c <= abs(nuevo):
        if nuevo != 0 and nuevo % c == 0:
            dos2 = dos2 + 1
        c = c + 1

    primo2 = 0
    if dos2 == 2:
        primo2 = 1

    if fibo2 == 1 and primo2 == 1:
        print("¡El segundo numero cumple! Es primo y Fibonacci.")
        
        if a < nuevo:
            inicio = a + 1
            fin = nuevo
        else:
            inicio = nuevo + 1
            fin = a

        if a < 0 or nuevo < 0:
            resultado = 1
            k = inicio
            while k < fin:
                resultado = resultado * k
                k = k + 1
            print("Al haber negativos, la multiplicacion de los intermedios es:", resultado)
        else:
            resultado = 0
            k = inicio
            while k < fin:
                resultado = resultado + k
                k = k + 1
            print("Al ser positivos/cero, la suma de los intermedios es:", resultado)

        if resultado % 2 != 0:
            operacion_final = resultado ** 2
            print("Como el resultado es IMPAR, elevado al cuadrado es:", operacion_final)
        else:
            operacion_final = resultado ** 3
            print("Como el resultado es PAR, elevado al cubo es:", operacion_final)

    else:
        print("El segundo numero NO cumple con ser primo y Fibonacci a la vez.")

    id_usuario = int(input("\nIngrese su ID: "))
    
    dia = int(input("Ingrese el dia (numero): "))
    mes_nombre = input("Ingrese el nombre del mes (ej: enero, febrero): ")
    anio = int(input("Ingrese el año (numero): "))

    fecha = [dia, mes_nombre, anio]
    print("Vector Fecha original:", fecha)

    mes_sacado = fecha[1]

    fecha[1] = id_usuario
    print("Vector Fecha modificado (con ID):", fecha)

    abecedario = "abcdefghijklmnopqrstuvwxyz"
    vocales = "aeiouAEIOU"

    i = 0
    while i < len(mes_sacado):
        letra = mes_sacado[i].lower()

        es_vocal = False
        v = 0
        while v < len(vocales):
            if letra == vocales[v]:
                es_vocal = True
            v = v + 1

        if es_vocal:
            tipo = "Vocal"
        else:
            tipo = "Consonante"

        posicion = 0
        j = 0
        while j < len(abecedario):
            if letra == abecedario[j]:
                posicion = j + 1
            j = j + 1

        print("Letra '" + letra + "' -> Tipo: " + tipo + " | Posicion en abecedario: " + str(posicion))
        i = i + 1

main()