
# Solicitar el nombre y los apellidos del usuario.
nombre = input("Escribe tu nombre: ").title()
apellido_paterno = input("Escribe tu apellido paterno: ").title()
apellido_materno = input("Escribe tu apellido materno: ").title()

# Convertir la edad a entero y las medidas a decimales.
edad = int(input("Escribe tu edad en años: "))
peso = float(input("Escribe tu peso en kilogramos: "))
estatura = float(input("Escribe tu estatura en metros: "))

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
