from datetime import date


fecha_actual = date.today()


dia = int(input("Ingrese su fecha de nacimiento.\nDia: "))
mes = int(input("Mes: "))
anno = int(input("Anno: "))

edad = fecha_actual.year - anno


if fecha_actual.month < mes or (fecha_actual.month == mes and fecha_actual.day < dia):
    edad -= 1

print("Usted tiene", edad, "annos")