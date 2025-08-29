print ("Hola, promediaremos tu calificación final")

cal1= int(input("Por favor, indque su primera calificación: "))
print ("Tu primera calificación es : ", cal1)
cal2= int(input("Por favor, indque su segunda calificación: "))
print ("Tu segunda calificación es : ", cal2)
cal3= int(input("Por favor, indque su tercera calificación: "))
print ("Tu tercera calificación es : ", cal3)

#Sacaremos las medias de las tres calificaciones
calfin = (cal1+cal2+cal3)/3
print("Tu calificación final es de :",calfin)

#Utilizaremos la funcion if para indicarle al estudiante si obtuvo una calificación aprobatoria
if calfin >= 7:
    print ("Tu resultado final de :", calfin, "es aprobatorio")
elif calfin > 7:
    print ("Tu resultado final de : ", calfin, "es NO aprobatorio")

