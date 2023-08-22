dividendo = int(input("Introduce el dividendo: "))
divisor = int(input("Introduce el divisor: "))

cociente = dividendo // divisor
resto = dividendo % divisor

if resto == 0:
    print("La división es exacta")
else:
    print("La división no es exacta")

print("Cociente:", cociente)
print("Resto:", resto)