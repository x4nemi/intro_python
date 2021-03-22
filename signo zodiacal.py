dia = int(input("Día de nacimiento: "))
mes = int(input("Mes de nacimiento: "))
mes -= 1

signo = ["Acuario", "Piscis", "Aries", "Tauro", "Géminis", "Cancer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario", "Capricornio"]
i = 0

#no toma el rango dentro del for
if dia < 21 and mes == 0:
    print("Eres", signo[11])

else:
    for s in signo:
        if(dia > 20 and mes == i) or (dia < 21 and mes == i + 1):
            print("Eres", signo[i])
        i += 1