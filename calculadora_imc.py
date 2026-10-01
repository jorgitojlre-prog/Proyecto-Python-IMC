# Solicitar el nombre y los apellidos del usuario.
nombre = input("Escribe tu nombre: ")
apellido_paterno = input("Escribe tu apellido paterno: ")
apellido_materno = input("Escribe tu apellido materno: ")

# Convertir la edad a entero y las medidas a decimales.
edad = int(input("Escribe tu edad en años: "))
peso = float(input("Escribe tu peso en kilogramos: "))
estatura = float(input("Escribe tu estatura en metros: "))

# Calcular el índice de masa corporal.
imc = peso / estatura ** 2

# Mostrar los datos y el resultado con dos decimales.
print("\n¡Bienvenido a la calculadora de IMC!")
print("Usuario:", nombre, apellido_paterno, apellido_materno)
print("Edad:", edad, "años")
print("Peso:", peso, "kg")
print("Estatura:", estatura, "metros")
print(f"Tu IMC es: {imc:.2f}")