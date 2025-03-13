def binary_division(dividend, divisor):
    # Convertimos binarios en enteros
    dividend_int = int(dividend, 2)
    divisor_int = int(divisor, 2)
    
    # Inicializamos las variables
    remainder = dividend_int
    quotient = 0
    divisor_len = len(divisor)
    
    # Creamos la cantidad de espacios iniciales para alinear la primera resta
    spacing = len(dividend) - len(divisor)

    # Imprimir encabezado
    print(f"\nDividiendo {dividend} por {divisor}\n")
    
    # Procesamos bit a bit
    for i in range(len(dividend) - divisor_len + 1):
        # Desplazamos el divisor a la posición actual
        shifted_divisor = divisor_int << (len(dividend) - divisor_len - i)
        
        # Mostramos el valor actual del dividendo parcial alineado correctamente
        remainder_bin = bin(remainder)[2:].zfill(len(dividend))
        print(f"{' ' * (i + spacing)}{remainder_bin}")

        # Comparamos si el dividendo parcial es mayor o igual al divisor
        if remainder >= shifted_divisor:
            remainder -= shifted_divisor
            quotient |= 1 << (len(dividend) - divisor_len - i)

        # Mostramos el divisor desplazado alineado debajo del dividendo
        shifted_divisor_bin = bin(shifted_divisor)[2:].zfill(len(dividend))
        print(f"{' ' * (i + spacing)}-{shifted_divisor_bin}")
        print(f"{' ' * (i + spacing)}{'-' * len(dividend)}")

    # Convertimos el cociente y el residuo de nuevo a binarios
    quotient_bin = bin(quotient)[2:]
    remainder_bin = bin(remainder)[2:]

    # Imprimir resultado
    print(f"\nCociente: {quotient_bin}")
    print(f"Residuo: {remainder_bin}\n")

# Entrada: dividendo y divisor en formato binario
dividendo = "10110101000101"
divisor = "1011"

# Llamamos a la función de división
binary_division(dividendo, divisor)