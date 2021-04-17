
nome= input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
Altura = float(input("Digite sua altura: "))

IMC = (peso / (Altura*2))

if IMC > 25:

    print("Olá {}, Atenção!!! Seu IMC é igual: {:.2f}! Resultado Acima do normal" .format(nome,IMC))

elif  IMC < 20:
    print("Olá {}, Parabéns!!! Seu IMC é igual: {:.2f}! Resultado abaixo do normal" .format(nome,IMC))

else:
    print("Olá {}, Atenção!!! Seu IMC é igual: {:.2f}! Resultado normal" .format(nome,IMC))
    



