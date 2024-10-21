class MyHash:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = [-1] * tamano

    def funcion_hash(self, clave):
        return clave % self.tamano

    def insertar(self, clave):
        indice = self.funcion_hash(clave)
        while self.tabla[indice] != -1:
            indice = (indice + 1) % self.tamano
        self.tabla[indice] = clave

    def buscar(self, clave):
        indice = self.funcion_hash(clave)
        for _ in range(self.tamano):
            if self.tabla[indice] == clave:
                return indice
            indice = (indice + 1) % self.tamano
        return -1

    def imprimir_tabla(self):
        print("Tabla Hash:")
        for i, val in enumerate(self.tabla):
            print(f"Índice {i}: {val}")

def busqueda_secuencial(numeros, n):
    for k in range(len(numeros)):
        if numeros[k] == n:
            return k
    return -1

def busqueda_binaria(numeros, n):
    i = 0
    j = len(numeros) - 1
    while i <= j:
        intermedio = (i + j) // 2
        if numeros[intermedio] == n:
            return intermedio
        elif numeros[intermedio] > n:
            j = intermedio - 1
        else:
            i = intermedio + 1
    return -1

def busqueda_binaria_recursiva(numeros, n, i, j):
    intermedio = (i + j) // 2
    if i > j:
        return -1
    elif numeros[intermedio] == n:
        return intermedio
    elif numeros[intermedio] > n:
        return busqueda_binaria_recursiva(numeros, n, i, intermedio - 1)
    else:
        return busqueda_binaria_recursiva(numeros, n, intermedio + 1, j)

numeros = [4, 5, 7, 8, 9, 15, 30]
n = int(input("Número a buscar: "))

resultado = busqueda_secuencial(numeros, n)
print("Búsqueda secuencial:", resultado)

r = busqueda_binaria(numeros, n)
print("Búsqueda binaria:", r)

r_recursivo = busqueda_binaria_recursiva(numeros, n, 0, len(numeros) - 1)
print("Búsqueda binaria recursiva:", r_recursivo)

# Uso de la clase MyHash
hash_table = MyHash(len(numeros) * 2)  # Doble tamaño para evitar colisiones
for num in numeros:
    hash_table.insertar(num)

hash_table.imprimir_tabla()

r_hash = hash_table.buscar(n)
print("Búsqueda basada en hash:", r_hash)