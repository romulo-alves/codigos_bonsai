altura = 0
sexo = 0
IMC = 0

print ("Digitte sua altura (em cm)")

altura = float(input())

altura = altura / 100

print ("Qual seu sexo? (M) ou (F)")

sexo = input()

if sexo == 'M':
    IMC = (72.7*altura)-58
    print ("IMC = %.1f" % IMC, "kg")

elif sexo == 'm':
    IMC = (72.7*altura)-58
    print ("IMC = %.1f" % IMC, "kg")

elif sexo == 'F':
    IMC = (62.1*altura)-44.7
    print ("IMC = %.1f" % IMC, "kg")

elif sexo == 'f':
    IMC = (62.1*altura)-44.7
    print ("IMC = %.1f" % IMC, "kg")

