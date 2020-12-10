print ("Escreva a área a ser pintada? (em m²)")

area_pintada = int(input())

litros_de_tinta = (area_pintada / 6)

print ("Litros necessários", litros_de_tinta)
print ("")

#latas (18 litros)

print ("LATAS")
print ("")

quantidade_latas = round(litros_de_tinta/18+0.5)

valor_latas = quantidade_latas * 80

print ("Nº de latas:", quantidade_latas)
print ("Valor total: R$ %.2f" % valor_latas)
print ("")

#galões (3,6 litros)

print ("GALÕES")
print ("")

quantidade_galoes = round(litros_de_tinta/3.6+0.5)

valor_galoes = quantidade_galoes * 25

print ("Nº de galões:", quantidade_galoes)
print ("Valor total: R$ %.2f" % valor_galoes)

#latas e galoes

print ("LATAS E GALÕES")
print ("")

litros_de_tinta = (area_pintada / 6) * 1.10

latas = round((litros_de_tinta//18))

valor_final_latas = latas * 80

sobra_tinta = litros_de_tinta%18

valor_latas = quantidade_latas * 80

print ("Nº de latas:", latas)
print ("Valor total: R$ %.2f" % valor_final_latas)

galoes = round((sobra_tinta/3.6)+0.5)

valor_final_galoes = galoes * 25

print ("Nº de galões:", galoes)
print ("Valor total: R$ %.2f" % valor_final_galoes)





