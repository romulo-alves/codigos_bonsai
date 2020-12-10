altura = 0
sexo = 0 # Essa linha não é necessária. Quando você diz que sexo = 0 passa a ideia de
         # que você vai utilizar alguma representação numerica para o sexo
         # Se quiser definir a variavel aqui é melhor usar sexo = "" (string vazia) para deixar explicito que
         # sexo é uma string
IMC = 0

print ("Digitte sua altura (em cm)")

altura = float(input())

altura = altura / 100

print ("Qual seu sexo? (M) ou (F)")

sexo = input()


if sexo == 'M': # você pode usar o mesmo if tanto para a letra maiuscula quanto pra minuscula usando 'or'
    IMC = (72.7*altura)-58
    #Evite repetição de código. Veja que o print é o mesmo código em todos os if
    #você pode fazer o print fora dos if
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

