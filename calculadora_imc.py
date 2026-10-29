
# Solicitar el nombre y los apellidos sin permitir campos vacíos.
while True:
    nombre = input("Escribe tu nombre: ").strip().title()
    if nombre:
        break
    print("Error: El nombre no puede estar vacío.")

while True:
    apellido_paterno = input("Escribe tu apellido paterno: ").strip().title()
    if apellido_paterno:
        break
    print("Error: El apellido paterno no puede estar vacío.")

while True:
    apellido_materno = input("Escribe tu apellido materno: ").strip().title()
    if apellido_materno:
        break
    print("Error: El apellido materno no puede estar vacío.")

# Validar que edad, peso y estatura sean números positivos.
while True:
    try:
        edad = int(input("Escribe tu edad en años: "))
        if edad > 0:
            break
        print("Error: La edad debe ser mayor que cero.")
    except ValueError:
        print("Error: Escribe una edad válida en números.")

while True:
    try:
        peso = float(input("Escribe tu peso en kilogramos: "))
        if peso > 0:
            break
        print("Error: El peso debe ser mayor que cero.")
    except ValueError:
        print("Error: Escribe un peso válido en números.")

while True:
    try:
        estatura = float(input("Escribe tu estatura en metros: "))
        if estatura > 0:
            break
        print("Error: La estatura debe ser mayor que cero.")
    except ValueError:
        print("Error: Escribe una estatura válida en números.")

# Calcular el índice de masa corporal.
imc = peso / estatura ** 2

# Mostrar los datos y el resultado con dos decimales.
print("\n===================================")
print("          REPORTE DE IMC")
print("===================================")

print(f"Nombre: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso:.2f} kg")
print(f"Estatura: {estatura:.2f} metros")
print("-----------------------------------")
print(f"Tu IMC es: {imc:.2f}")
print("===================================")
