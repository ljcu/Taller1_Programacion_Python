caracter = input("Introduce un caracter: ")

if caracter.isalpha():
    if caracter.isupper():
        print("El caracter es una letra mayúscula")
    else:
        print("El caracter es una letra minúscula")
elif caracter.isdigit():
    print("El caracter es un número")
else:
    print("El caracter no es ni letra ni número")