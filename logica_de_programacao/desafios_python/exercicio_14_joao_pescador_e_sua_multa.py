print ("Qual a quantidade de peixes? (em kg)")

peso_do_peixe = float(input())

excesso = peso_do_peixe - 50

multa = 0

if excesso > 0:
    multa = excesso * 4
    print ("Você deve pagar R$ %.2f" % multa, "de multa por excesso de peso")

else:
    print ("Você não precisa pagar nada!")



