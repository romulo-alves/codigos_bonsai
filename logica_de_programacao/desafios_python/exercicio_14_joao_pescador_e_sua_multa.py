print ("Qual a quantidade de peixes? (em kg)")

peso_do_peixe = float(input()) # bom nome da variável

excesso = peso_do_peixe - 50 # O número 50 pode ser armazenado em uma variável

multa = 0

if excesso > 0:
    multa = excesso * 4
    print ("Você deve pagar R$ %.2f" % multa, "de multa por excesso de peso")

else:
    print ("Você não precisa pagar nada!")



