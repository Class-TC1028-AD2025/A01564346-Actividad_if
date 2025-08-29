
print("Hola, bienvenido a los eventos del día de hoy")
edad = int(input("Por favor indica tu edad: "))
print("Tu edad es:", edad)

#Evaluamos la edad, para seleccionar el tipo de evento al que tienen acceso
if edad>=18:
    print("Puedes acceder al evento para adultos y evento familiar")
elif edad > 13:
    print("Puedes acceder al evento familiar y de jovenes")
else:
    print("Lo siento, unicamente puedes acceder al evento familiar")

print("¡Gracias por acompañarnos!")
