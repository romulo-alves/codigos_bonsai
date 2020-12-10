print ("Escreva a área a ser pintada? (em m²)")

area_pintada = int(input())

litros_de_tinta = (area_pintada / 6) # O que esse 6 significa? É uma boa prática colocar em uma variável com nome significativo

print ("Litros necessários", litros_de_tinta)
print ("")

#latas (18 litros)

print ("LATAS")
print ("")

quantidade_latas = round(litros_de_tinta/18+0.5)

valor_latas = quantidade_latas * 80 # Você pode criar uma variavel preco_da_lata para armazenar o 80

print ("Nº de latas:", quantidade_latas)
print ("Valor total: R$ %.2f" % valor_latas)
print ("")

#galões (3,6 litros)

print ("GALÕES")
print ("")

quantidade_galoes = round(litros_de_tinta/3.6+0.5)

valor_galoes = quantidade_galoes * 25 # O 25 pode ser colocado em uma variavel

print ("Nº de galões:", quantidade_galoes)
print ("Valor total: R$ %.2f" % valor_galoes)

#latas e galoes

print ("LATAS E GALÕES")
print ("")

# Coloque os valores em variáveis
# É difícil saber o que cada uma dessas formulas faz somente
# com vendo os números


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





