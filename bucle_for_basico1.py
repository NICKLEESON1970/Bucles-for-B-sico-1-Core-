# bucle_for_basico1.py

### Ejercicio 1: Básico
print("### Ejercicio 1: Básico")
print("Todos los números enteros del 0 al 100:")
for i in range(101):  # El límite superior en range() es exclusivo, por eso usamos 101
    print(i)

print("\n------------------------\n")

### Ejercicio 2: Múltiples de 2
print("### Ejercicio 2: Múltiples de 2")
print("Todos los números múltiplos de 2 entre 2 y 500:")
for i in range(2, 501, 2):  # range(inicio, fin, paso)
    print(i)

print("\n------------------------\n")

### Ejercicio 3: Contando Vanilla Ice
print("### Ejercicio 3: Contando Vanilla Ice")
print("Números del 1 al 100, con 'ice ice' por múltiplos de 5 y 'baby' por múltiplos de 10:")
for i in range(1, 101):
    if i % 10 == 0:  # Primero revisamos el múltiplo de 10 para evitar imprimir "ice ice" en lugar de "baby"
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

print("\n------------------------\n")

### Ejercicio 4: Wow. Número gigante a la vista
print("### Ejercicio 4: Wow. Número gigante a la vista")
print("Suma de los números pares del 0 al 500,000:")
suma_pares = sum(range(0, 500001, 2))  # Usamos sum() con range() para sumar todos los pares
print("Suma total:", suma_pares)

print("\n------------------------\n")

### Ejercicio 5: Regrésame al 3
print("### Ejercicio 5: Regrésame al 3")
print("Contador regresivo de 3 en 3 desde 2024:")
for i in range(2024, 0, -3):  # Contador regresivo con paso -3
    print(i)

print("\n------------------------\n")

### Ejercicio 6: Contador dinámico
print("### Ejercicio 6: Contador dinámico")
numInicial = 3
numFinal = 10
multiplo = 2
print(f"Números enteros múltiplos de {multiplo} desde {numInicial} hasta {numFinal}:")
for i in range(numInicial, numFinal + 1):  # Incluimos numFinal en el rango
    if i % multiplo == 0:
        print(i)