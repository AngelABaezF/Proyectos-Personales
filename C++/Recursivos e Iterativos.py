def fact_recur(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_recur(n - 1)

def fact_ite(n):
    rest = 1
    for i in range(2, n + 1):
        rest *= i
    return rest

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def pot(n):
    if n == 1:
            return True
    if n < 1 or n % 2 != 0:
        return False
    return pot(n//2)

numero = int(input("Introduce un numero para calcular su factorial, el fibonacci y te diga si es potencia de 2: "))

print(f"Factorial (recursivo) de {numero}: {fact_recur(numero)}")
print(f"Factorial (iterativo) de {numero}: {fact_ite(numero)}")
print(f"Fibonacci (recursivo) de {numero}: {fib(numero)}")
print(f"Potencia de dos (recursivo) de {numero}: {pot(numero)}")